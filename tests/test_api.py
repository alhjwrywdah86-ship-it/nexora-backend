def test_register_hides_password_hash(client):

    res = client.post(
        "/auth/register",
        json={
            "name": "Ali",
            "email": "ali@example.com",
            "password": "password123",
        },
    )

    assert res.status_code == 201
    assert "password_hash" not in res.json()


def test_duplicate_email_returns_409(client):

    user = {
        "name": "Ali",
        "email": "ali@example.com",
        "password": "password123",
    }

    client.post("/auth/register", json=user)
    res = client.post("/auth/register", json=user)

    assert res.status_code == 409


def test_wrong_password_returns_401(client):

    client.post(
        "/auth/register",
        json={
            "name": "Ali",
            "email": "ali@example.com",
            "password": "password123",
        },
    )

    res = client.post(
        "/auth/login",
        json={
            "email": "ali@example.com",
            "password": "wrong-password",
        },
    )

    assert res.status_code == 401


def test_goals_require_token(client):

    res = client.post("/goals", json={"title": "x"})

    assert res.status_code in (401, 403)


def test_create_goal_and_complete_task(client, auth_headers):

    res = client.post(
        "/goals",
        json={"title": "Learn English"},
        headers=auth_headers,
    )

    assert res.status_code == 200

    task_id = res.json()["tasks"][0]["id"]

    done = client.patch(
        f"/tasks/{task_id}/complete",
        headers=auth_headers,
    )

    assert done.status_code == 200
    assert done.json()["status"] == "completed"


def test_cannot_complete_other_users_task(client, auth_headers):

    res = client.post(
        "/goals",
        json={"title": "Private goal"},
        headers=auth_headers,
    )

    task_id = res.json()["tasks"][0]["id"]

    client.post(
        "/auth/register",
        json={
            "name": "Other",
            "email": "other@example.com",
            "password": "password123",
        },
    )

    login = client.post(
        "/auth/login",
        json={
            "email": "other@example.com",
            "password": "password123",
        },
    )

    other = {
        "Authorization": f"Bearer {login.json()['access_token']}"
    }

    done = client.patch(
        f"/tasks/{task_id}/complete",
        headers=other,
    )

    assert done.status_code == 404


def test_dashboard(client, auth_headers):

    client.post(
        "/goals",
        json={"title": "Goal"},
        headers=auth_headers,
    )

    res = client.get("/dashboard", headers=auth_headers)

    assert res.status_code == 200
    assert res.json()["active_goals"] == 1
