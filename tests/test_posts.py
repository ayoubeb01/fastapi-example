from typing import List
from app import schemas
import pytest
def test_get_all_posts(authorized_client,test_posts):
    res=authorized_client.get("/posts/")
    
    def validate(post: dict):
        return schemas.PostOut(**post)

    posts_map= map(validate,res.json())
    #print(list(posts_map))
    posts_list= list(posts_map)
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    

def test_unauthorized_user_get_all_posts(client,test_posts):
    res = client.get('/posts/')
    assert res.status_code == 401



def test_unauthorized_user_get_one_post(client,test_posts):
    res = client.get(f'/posts/{test_posts[0].id}')
    assert res.status_code == 401



def test_get_one_post_not_exist(authorized_client,test_posts):
    res = authorized_client.get('/posts/88888')
    assert res.status_code == 404




def test_get_one_post_(authorized_client,test_posts):
    res = authorized_client.get(f'/posts/{test_posts[0].id}')
    #print(res.json())
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content
    assert res.status_code == 200


@pytest.mark.parametrize('title, content, published',[
    ("awesome new titlte","awesome new content",True),
    ("favorite pizza","i love pepporoni",False),
    ("tallest skyscrapers","wahoo",True)])
def test_create_post(authorized_client, test_user, test_posts,title,content,published):
    res = authorized_client.post('/posts/',json=
                                 {'title':title,
                                  'content':content,
                                  'published':published})
    #print(res.status_code)
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert int(created_post.owner_id) == test_user['id']

def test_create_post_default_published_true(authorized_client,test_user):
    res = authorized_client.post('/posts/',json=
                             {'title':"arbitrary title",
                              'content':'rrhuihrrjhrjjkrjrhjr'})
    #print(res.status_code)
    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == 'arbitrary title'
    assert created_post.content == 'rrhuihrrjhrjjkrjrhjr'
    assert created_post.published == True
    assert int(created_post.owner_id) == test_user['id']


def test_unauthorized_user_create_post(client,test_user):
    res = client.post('/posts/',json=
                             {'title':"arbitrary title",
                              'content':'rrhuihrrjhrjjkrjrhjr'})
    assert res.status_code == 401


def test_unauthorized_user_delete_post(client,test_user,test_posts):
    res = client.delete(f'/posts/{test_posts[0].id}')
    assert res.status_code == 401

def test_authorized_user_delete_post(authorized_client,test_user,test_posts):
    res = authorized_client.delete(f'/posts/{test_posts[0].id}')
    assert res.status_code == 204


def test_delete_post_not_exist(authorized_client,test_user,test_posts):
    res = authorized_client.delete(f'/posts/8888888888')
    assert res.status_code == 404


def test_delete_other_user_post(authorized_client, test_user,test_user2, test_posts):
    res = authorized_client.delete(f'/posts/{test_posts[3].id}')
    assert res.status_code == 403


def test_update_post(authorized_client, test_user, test_posts):
    data =  {'title':"updated post",
                              'content':'updated content',
                              'id':test_posts[0].id
                              }
    res = authorized_client.put(f'/posts/{test_posts[0].id}',json=data)
    update_post=schemas.Post(**res.json())
    assert res.status_code == 200
    assert update_post.title == data['title']
    assert update_post.content == data['content']



def test_update_other_user_post(authorized_client, test_user,test_user2, test_posts):
    data =  {'title':"updated post",
                              'content':'updated content',
                              'id':test_posts[3].id
                              }
    res = authorized_client.put(f'/posts/{test_posts[3].id}',json=data)
    assert res.status_code == 403


def test_unauthorized_user_update_post(client,test_user,test_posts):
    res = client.put(f'/posts/{test_posts[3].id}')
    assert res.status_code == 401



def test_update_post_not_exist(authorized_client,test_user,test_posts):
    data =  {'title':"updated post",
                              'content':'updated content',
                              'id':test_posts[3].id
                              }
    res = authorized_client.put(f'/posts/8888888888',json=data)
    assert res.status_code == 404

