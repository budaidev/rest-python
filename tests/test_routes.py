"""Test module for the Flask REST API routes."""

import json
import pytest
from app import app
from app.routes import items  # Import items list to clear it between tests

@pytest.fixture
def client():
    """Create a test client fixture for the Flask application.
    
    Returns:
        Flask test client with a clean state.
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Clear items before each test
        items.clear()
        yield client

def test_health_check(client):
    """Verify that the health check endpoint returns a healthy status."""
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}

def test_get_items_empty(client):
    """Verify that getting items returns an empty list when no items exist."""
    response = client.get('/api/items')
    assert response.status_code == 200
    assert response.json == {'items': []}

def test_create_item(client):
    """Verify that creating a new item works correctly."""
    response = client.post('/api/items',
                         data=json.dumps({'name': 'Test Item'}),
                         content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == 'Item created'
    assert response.json['item']['name'] == 'Test Item'
    assert response.json['item']['id'] == 1

def test_create_item_invalid_data(client):
    """Verify that creating an item with invalid data returns an error."""
    response = client.post('/api/items',
                         data=json.dumps({}),
                         content_type='application/json')
    assert response.status_code == 400
    assert response.json['error'] == 'Invalid request data'

def test_get_items_after_create(client):
    """Verify that getting items after creation returns the correct item."""
    # First create an item
    client.post('/api/items',
               data=json.dumps({'name': 'Test Item'}),
               content_type='application/json')
    
    # Then get all items
    response = client.get('/api/items')
    assert response.status_code == 200
    assert len(response.json['items']) == 1
    assert response.json['items'][0]['name'] == 'Test Item'

def test_get_single_item(client):
    """Verify that getting a single item returns the correct item details."""
    # First create an item
    client.post('/api/items',
               data=json.dumps({'name': 'Test Item'}),
               content_type='application/json')
    
    # Then get it by id
    response = client.get('/api/items/1')
    assert response.status_code == 200
    assert response.json['item']['name'] == 'Test Item'

def test_get_nonexistent_item(client):
    """Verify that getting a nonexistent item returns a 404 error."""
    response = client.get('/api/items/999')
    assert response.status_code == 404
    assert response.json['error'] == 'Item not found'

def test_update_item(client):
    """Verify that updating an item changes its data correctly."""
    # First create an item
    client.post('/api/items',
               data=json.dumps({'name': 'Test Item'}),
               content_type='application/json')
    
    # Then update it
    response = client.put('/api/items/1',
                        data=json.dumps({'name': 'Updated Item'}),
                        content_type='application/json')
    assert response.status_code == 200
    assert response.json['item']['name'] == 'Updated Item'

def test_delete_item(client):
    """Verify that deleting an item removes it from storage."""
    # First create an item
    client.post('/api/items',
               data=json.dumps({'name': 'Test Item'}),
               content_type='application/json')
    
    # Then delete it
    response = client.delete('/api/items/1')
    assert response.status_code == 200
    assert response.json['message'] == 'Item deleted'
    
    # Verify it's gone
    response = client.get('/api/items/1')
    assert response.status_code == 404
