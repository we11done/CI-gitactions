create_user = """
    mutation MyMutation {
        addUser(name: "test") {
            ... on User {
            id
            name
            }
            ... on UserExists {
            message
            }
        }
    }
"""

delete_specific_user = """
mutation MyMutation {
  deleteUser(userId: 1) {
    ... on UserDeleted {
      message
    }
    ... on UserNotFound {
      message
    }
    ... on UserIdMissing {
      message
    }
  }
}
"""
