get_users_query = """
query MyQuery {
  users {
    id
    name
  }
}
"""

get_specific_user_query = """
query MyQuery2 {
  user(userId: 1) {
    id
    name
  }
}
"""
