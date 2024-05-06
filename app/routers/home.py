from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def get_user():
    """
    Get a user by ID.

    This route retrieves information about a user based on their ID provided in the URL path.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: A dictionary containing user information (replace with actual data).
    """

    # Replace this with your logic to retrieve user data from database or other source
    user_data = {"id": 1, "name": "John Doe", "email": "johndoe@example.com"}

    return user_data
