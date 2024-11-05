import json
import pytest
from app import app
from app.routes import items  # Import items list to clear it between tests

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Clear items before each test
        items.clear()
        yield client

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}

def test_get_items_empty(client):
    """Test getting items when none exist"""
    response = client.get('/api/items')
    assert response.status_code == 200
    assert response.json == {'items': []}

def test_create_item(client):
    """Test creating a new item"""
    response = client.post('/api/items',
                         data=json.dumps({'name': 'Test Item'}),
                         content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == 'Item created'
    assert response.json['item']['name'] == 'Test Item'
    assert response.json['item']['id'] == 1

def test_create_item_invalid_data(client):
    """Test creating an item with invalid data"""
    response = client.post('/api/items',
                         data=json.dumps({}),
                         content_type='application/json')
    assert response.status_code == 400
    assert response.json['error'] == 'Invalid request data'

def test_get_items_after_create(client):
    """Test getting items after creating one"""
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
    """Test getting a single item"""
    # First create an item
    client.post('/api/items',
               data=json.dumps({'name': 'Test Item'}),
               content_type='application/json')
    
    # Then get it by id
    response = client.get('/api/items/1')
    assert response.status_code == 200
    assert response.json['item']['name'] == 'Test Item'

def test_get_nonexistent_item(client):
    """Test getting an item that doesn't exist"""
    response = client.get('/api/items/999')
    assert response.status_code == 404
    assert response.json['error'] == 'Item not found'

def test_update_item(client):
    """Test updating an item"""
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
    """Test deleting an item"""
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
