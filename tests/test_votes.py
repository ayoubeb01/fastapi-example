import pytest
from app import models


@pytest.fixture()
def test_vote(test_posts,session,test_user):
    new_vote=models.Vote(post_id =test_posts[3].id,user_id=test_user['id'])
    session.add(new_vote)
    session.commit()



def test_vote_on_post(authorized_client,test_posts):
    res = authorized_client.post('/vote/',json={"post_id":test_posts[0].id,"dir":1})
    res.status_code == 201


def test_vote_twice_post(authorized_client,test_posts,test_vote):
    res = authorized_client.post('/vote/',json={"post_id":test_posts[3].id,"dir":1})
    res.status_code == 409


def test_delete_vote(authorized_client,test_posts):
    res = authorized_client.delete(f'/vote/{test_posts[3].id}')
    res.status_code == 200


def test_delete_vote_not_exist(authorized_client,test_posts):
    res = authorized_client.delete(f'/vote/888888888888888')
    res.status_code == 404



def test_delete_vote_post_not_exist(authorized_client,test_posts):
    res = authorized_client.post('/vote/',json={"post_id":8000000,"dir":1})
    res.status_code == 404


def test_vote_unauthorized(client,test_posts):
    res = client.post('/vote/',json={"post_id":test_posts[0].id,"dir":1})
    res.status_code == 401
