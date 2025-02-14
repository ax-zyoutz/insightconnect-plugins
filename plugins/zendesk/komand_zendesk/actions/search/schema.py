# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Search Zendesk"


class Input:
    ITEM = "item"
    TYPE = "type"
    

class Output:
    ORGANIZATIONS = "organizations"
    TICKETS = "tickets"
    USERS = "users"
    

class SearchInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "item": {
      "type": "string",
      "title": "Item",
      "description": "Search item E.g. password reset",
      "order": 2
    },
    "type": {
      "type": "string",
      "title": "Type",
      "description": "Search type",
      "enum": [
        "User",
        "Organization",
        "Ticket"
      ],
      "order": 1
    }
  },
  "required": [
    "item",
    "type"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "organizations": {
      "type": "array",
      "title": "Organization Search Results",
      "description": "Get Zendesk query results for organizations",
      "items": {
        "$ref": "#/definitions/organization"
      },
      "order": 2
    },
    "tickets": {
      "type": "array",
      "title": "Ticket Search Results",
      "description": "Get Zendesk query results for tickets",
      "items": {
        "$ref": "#/definitions/ticket"
      },
      "order": 1
    },
    "users": {
      "type": "array",
      "title": "User Search Results",
      "description": "Get Zendesk query results for users",
      "items": {
        "$ref": "#/definitions/user"
      },
      "order": 3
    }
  },
  "definitions": {
    "comment": {
      "type": "object",
      "title": "comment",
      "properties": {
        "author_id": {
          "type": "string",
          "title": "Author ID",
          "description": "Author ID",
          "order": 4
        },
        "body": {
          "type": "string",
          "title": "Body",
          "description": "Comment body",
          "order": 1
        },
        "html_body": {
          "type": "string",
          "title": "HTML Body",
          "description": "The comment formatted as HTML. This will be preferred over body",
          "order": 2
        },
        "public": {
          "type": "boolean",
          "title": "Public",
          "description": "Public (true if public comment, false if an internal note)",
          "order": 3
        }
      }
    },
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    },
    "organization": {
      "type": "object",
      "title": "organization",
      "properties": {
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Created at",
          "format": "date-time",
          "order": 1
        },
        "details": {
          "type": "string",
          "title": "Details",
          "description": "Details",
          "order": 2
        },
        "external_id": {
          "type": "string",
          "title": "External ID",
          "description": "External ID",
          "order": 3
        },
        "group_id": {
          "type": "string",
          "title": "Group ID",
          "description": "Group ID",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 5
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 6
        },
        "notes": {
          "type": "string",
          "title": "Notes",
          "description": "Notes",
          "order": 7
        },
        "shared_comments": {
          "type": "boolean",
          "title": "Shared Comments",
          "description": "Shared comments",
          "order": 8
        },
        "shared_tickets": {
          "type": "boolean",
          "title": "Shared Tickets",
          "description": "Shared tickets",
          "order": 9
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "type": "string"
          },
          "order": 10
        },
        "updated_at": {
          "type": "string",
          "title": "Updated At",
          "description": "Updated at",
          "order": 11
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 12
        }
      }
    },
    "ticket": {
      "type": "object",
      "title": "ticket",
      "properties": {
        "assignee_id": {
          "type": "string",
          "title": "Assignee ID",
          "description": "Assignee ID",
          "order": 2
        },
        "attachment": {
          "$ref": "#/definitions/file",
          "title": "Attachment",
          "description": "Attachment",
          "order": 1
        },
        "collaborator_ids": {
          "type": "array",
          "title": "Collaborator IDs",
          "description": "Collaborator IDs",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "comment": {
          "$ref": "#/definitions/comment",
          "title": "Comment",
          "description": "Comment",
          "order": 4
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 5
        },
        "due_at": {
          "type": "string",
          "title": "Due At",
          "displayType": "date",
          "description": "Due at",
          "format": "date-time",
          "order": 6
        },
        "external_id": {
          "type": "string",
          "title": "External ID",
          "description": "External ID",
          "order": 7
        },
        "group_id": {
          "type": "string",
          "title": "Group ID",
          "description": "Group ID",
          "order": 8
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 9
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "description": "Priority",
          "order": 16
        },
        "problem_id": {
          "type": "string",
          "title": "Problem ID",
          "description": "Problem ID",
          "order": 12
        },
        "recipient": {
          "type": "string",
          "title": "Recipient ID",
          "description": "Recipient ID",
          "order": 11
        },
        "requester_id": {
          "type": "string",
          "title": "Requester ID",
          "description": "Requester ID",
          "order": 10
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 17
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "description": "Subject",
          "order": 13
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "type": "string"
          },
          "order": 14
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 15
        }
      },
      "definitions": {
        "comment": {
          "type": "object",
          "title": "comment",
          "properties": {
            "author_id": {
              "type": "string",
              "title": "Author ID",
              "description": "Author ID",
              "order": 4
            },
            "body": {
              "type": "string",
              "title": "Body",
              "description": "Comment body",
              "order": 1
            },
            "html_body": {
              "type": "string",
              "title": "HTML Body",
              "description": "The comment formatted as HTML. This will be preferred over body",
              "order": 2
            },
            "public": {
              "type": "boolean",
              "title": "Public",
              "description": "Public (true if public comment, false if an internal note)",
              "order": 3
            }
          }
        },
        "file": {
          "id": "file",
          "type": "object",
          "title": "File",
          "description": "File Object",
          "properties": {
            "content": {
              "type": "string",
              "title": "Content",
              "description": "File contents",
              "format": "bytes"
            },
            "filename": {
              "type": "string",
              "title": "Filename",
              "description": "Name of file"
            }
          }
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "active": {
          "type": "boolean",
          "title": "Active",
          "description": "Active",
          "order": 1
        },
        "alias": {
          "type": "string",
          "title": "Alias",
          "description": "Alias",
          "order": 2
        },
        "chat_only": {
          "type": "boolean",
          "title": "Chat Only",
          "description": "Chat only",
          "order": 3
        },
        "created_at": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Created at",
          "format": "date-time",
          "order": 4
        },
        "custom_role_id": {
          "type": "string",
          "title": "Custom Role ID",
          "description": "Custom role ID",
          "order": 5
        },
        "details": {
          "type": "string",
          "title": "Details",
          "description": "Details",
          "order": 6
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 7
        },
        "external_id": {
          "type": "string",
          "title": "External ID",
          "description": "External ID",
          "order": 8
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 9
        },
        "last_login_at": {
          "type": "string",
          "title": "Last Login At",
          "displayType": "date",
          "description": "Last login at",
          "format": "date-time",
          "order": 10
        },
        "locale": {
          "type": "string",
          "title": "Locale",
          "description": "Locale",
          "order": 11
        },
        "locale_id": {
          "type": "integer",
          "title": "Locale ID",
          "description": "Locale ID",
          "order": 12
        },
        "moderator": {
          "type": "boolean",
          "title": "Moderator",
          "description": "Moderator",
          "order": 13
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 14
        },
        "notes": {
          "type": "string",
          "title": "Notes",
          "description": "Notes",
          "order": 15
        },
        "only_private_comments": {
          "type": "boolean",
          "title": "Only Private Comments",
          "description": "Only private comments",
          "order": 16
        },
        "organization_id": {
          "type": "string",
          "title": "Organization ID",
          "description": "Organization ID",
          "order": 17
        },
        "phone": {
          "type": "string",
          "title": "Phone",
          "description": "Phone",
          "order": 18
        },
        "photo": {
          "type": "object",
          "title": "Photo",
          "description": "Photo",
          "order": 19
        },
        "restricted_agent": {
          "type": "boolean",
          "title": "Restricted Agent",
          "description": "Restricted agent",
          "order": 20
        },
        "role": {
          "type": "string",
          "title": "Role",
          "description": "Role",
          "order": 21
        },
        "shared": {
          "type": "boolean",
          "title": "Shared",
          "description": "Shared",
          "order": 22
        },
        "shared_agent": {
          "type": "boolean",
          "title": "Shared Agent",
          "description": "Shared agent",
          "order": 23
        },
        "signature": {
          "type": "string",
          "title": "Signature",
          "description": "Signature",
          "order": 24
        },
        "suspended": {
          "type": "boolean",
          "title": "Suspended",
          "description": "Suspended",
          "order": 25
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "Tags",
          "items": {
            "type": "string"
          },
          "order": 26
        },
        "ticket_restriction": {
          "type": "string",
          "title": "Ticket Restriction",
          "description": "Ticket restriction",
          "order": 27
        },
        "time_zone": {
          "type": "string",
          "title": "Time Zone",
          "description": "Time Zone",
          "order": 28
        },
        "two_factor_auth_enabled": {
          "type": "boolean",
          "title": "Two Factor Auth Enabled",
          "description": "Two factor auth enabled",
          "order": 29
        },
        "updated_at": {
          "type": "string",
          "title": "Updated At",
          "description": "Updated at",
          "order": 30
        },
        "url": {
          "type": "string",
          "title": "URL",
          "description": "URL",
          "order": 31
        },
        "verified": {
          "type": "boolean",
          "title": "Verified",
          "description": "Verified",
          "order": 32
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
