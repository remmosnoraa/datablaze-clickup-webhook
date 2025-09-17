# datablaze-clickup-webhook

# Example:

{
  "id": "868fm5fyq",
  "custom_id": null,
  "custom_item_id": 0,
  "name": "New Task Name",
  "text_content": "",
  "description": "",
  "status": {
    "id": "sc901102682453_EacxDmNf",
    "status": "new assingment",
    "color": "#c6ff1a",
    "orderindex": 0,
    "type": "open"
  },
  "orderindex": "120304945.00000000000000000000000000000000",
  "date_created": "1758068595869",
  "date_updated": "1758068595967",
  "date_closed": null,
  "date_done": null,
  "archived": false,
  "creator": {
    "id": 44157906,
    "username": "Aaron Sommer",
    "color": "#4169e1",
    "email": "asommer@philalegal.org",
    "profilePicture": null
  },
  "assignees": [],
  "group_assignees": [],
  "watchers": [
    {
      "id": 44157906,
      "username": "Aaron Sommer",
      "color": "#4169e1",
      "initials": "AS",
      "email": "asommer@philalegal.org",
      "profilePicture": null
    }
  ],
  "checklists": [],
  "tags": [],
  "parent": null,
  "top_level_parent": null,
  "priority": null,
  "due_date": null,
  "start_date": null,
  "points": null,
  "time_estimate": null,
  "time_spent": 0,
  "custom_fields": [
    {
      "id": "dc0bf162-4b81-4a2b-9be6-d36b639cd201",
      "name": "Docket No.",
      "type": "short_text",
      "type_config": {},
      "date_created": "1721255608025",
      "hide_from_guests": false,
      "required": false
    },
    {
      "id": "995cc6b2-1d16-4f52-8aee-e1c22e17e7a2",
      "name": "_UN_",
      "type": "short_text",
      "type_config": {},
      "date_created": "1683235759629",
      "hide_from_guests": false,
      "required": false
    },
    {
      "id": "d2a1e92b-f49f-4e79-b87b-d52d219c87e2",
      "name": "~PW~",
      "type": "short_text",
      "type_config": {},
      "date_created": "1683235781613",
      "hide_from_guests": false,
      "required": false
    },
    {
      "id": "4c62f9c4-34a1-4b4c-91de-a09ff2caf4ab",
      "name": "🗓️ Add to calendar",
      "type": "checkbox",
      "type_config": {},
      "date_created": "1738168644520",
      "hide_from_guests": false,
      "required": false
    },
    {
      "id": "372810e6-9260-4a2d-8b3d-56cfc27f94ec",
      "name": "Casework",
      "type": "drop_down",
      "type_config": {
        "default": 0,
        "sorting": "manual",
        "placeholder": null,
        "new_drop_down": true,
        "options": [
          {
            "id": "72095b6a-9d66-493b-a377-37033cb03ecc",
            "name": "New Assignment",
            "color": "#b7ff0d",
            "orderindex": 0
          },
          {
            "id": "c8c41fd3-9acd-47ea-8a90-166be0bfc1d9",
            "name": "Troubleshooting",
            "color": "#ff6659",
            "orderindex": 1
          },
          {
            "id": "7614185b-6f97-4cd4-85c4-eed92f0e3cbc",
            "name": "Appeal",
            "color": "#068075",
            "orderindex": 2
          },
          {
            "id": "5d525d9a-802b-431a-ac5d-d09fb931770c",
            "name": "Reassigned",
            "color": "#995c4c",
            "orderindex": 3
          },
          {
            "id": "802ceb24-1799-4f97-b2fd-92bf45ff8950",
            "name": "Assistance Complete",
            "color": "#001901",
            "orderindex": 4
          }
        ]
      },
      "date_created": "1682630484065",
      "hide_from_guests": false,
      "value": 4,
      "value_richtext": null,
      "required": false
    },
    {
      "id": "05cdbbb0-6b81-4dd5-a3ec-1fdd86035348",
      "name": "Appeal Progression",
      "type": "drop_down",
      "type_config": {
        "sorting": "manual",
        "new_drop_down": true,
        "options": [
          {
            "id": "e29f293c-ba15-41ca-8a6a-b0e42d48b54b",
            "name": "DQ: Appeal Not Filed",
            "color": "#f33140",
            "orderindex": 0
          },
          {
            "id": "d2a1d14e-1939-411e-a861-923052a80430",
            "name": "REF: Appeal Filed",
            "color": "#268f99",
            "orderindex": 1
          },
          {
            "id": "b3e6d9de-cee9-42c3-86c9-a42861f4a702",
            "name": "REF: Post-Hearing",
            "color": "#39bae6",
            "orderindex": 2
          },
          {
            "id": "89534258-e250-42d9-9fa3-a20b0d966f5d",
            "name": "UCBR: Appeal/Briefing",
            "color": "#265699",
            "orderindex": 3
          },
          {
            "id": "8d8559fc-90d2-4d08-a4aa-ce0787dd336c",
            "name": "UCBR: Decision",
            "color": "#3964e6",
            "orderindex": 4
          },
          {
            "id": "edb6110c-b284-4ddd-a350-641e4c727232",
            "name": "CC: Review/PFR",
            "color": "#282080",
            "orderindex": 5
          },
          {
            "id": "a5fe4cd1-4eb6-46c8-9679-e1397b32e43c",
            "name": "CC: Briefing",
            "color": "#4929a6",
            "orderindex": 6
          },
          {
            "id": "cd992028-9a8d-4c23-ab10-13b79e816853",
            "name": "CC: Argument",
            "color": "#7333cc",
            "orderindex": 7
          },
          {
            "id": "671321d0-ca8d-4466-9151-d6389f48d6a2",
            "name": "CC: Decision",
            "color": "#a73df2",
            "orderindex": 8
          },
          {
            "id": "35968f30-c4ed-4dfa-bd18-75adee803f66",
            "name": "SCOPA: Petition for Appeal",
            "color": "#782080",
            "orderindex": 9
          },
          {
            "id": "637c27c2-8b80-492d-a749-dde6115496ae",
            "name": "SCOPA: Briefing",
            "color": "#a6299b",
            "orderindex": 10
          },
          {
            "id": "290c228a-d673-424f-9ff9-39b4538cdc49",
            "name": "SCOPA: Argument",
            "color": "#cc33a6",
            "orderindex": 11
          },
          {
            "id": "0dc328b9-f869-406b-9cd3-82d935519d12",
            "name": "SCOPA: Decision",
            "color": "#f23da7",
            "orderindex": 12
          }
        ]
      },
      "date_created": "1682692555248",
      "hide_from_guests": false,
      "required": false
    },
    {
      "id": "7124a185-1d82-4c13-a41e-4327aaf9adda",
      "name": "Retainer/Citizenship Attest?",
      "type": "checkbox",
      "type_config": {},
      "date_created": "1708553832825",
      "hide_from_guests": false,
      "required": false
    },
    {
      "id": "cc2c56d8-5bd6-47c3-ae15-b53e1b4d186d",
      "name": "First Name",
      "type": "short_text",
      "type_config": {},
      "date_created": "1721251735301",
      "hide_from_guests": false,
      "value": "First",
      "value_richtext": null,
      "required": false
    },
    {
      "id": "6bddcd8d-3d19-4ed1-8159-8f7a47ea5ed1",
      "name": "Last Name",
      "type": "short_text",
      "type_config": {},
      "date_created": "1708966075985",
      "hide_from_guests": false,
      "value": "Last",
      "value_richtext": null,
      "required": false
    },
    {
      "id": "eff6a583-46d3-4da6-8bca-a6a183b528fa",
      "name": "LS File",
      "type": "url",
      "type_config": {},
      "date_created": "1682950003065",
      "hide_from_guests": false,
      "required": false
    },
    {
      "id": "1c22edaa-ee48-46cd-8db1-a42b470aabb5",
      "name": "Phone #",
      "type": "phone",
      "type_config": {},
      "date_created": "1682951493718",
      "hide_from_guests": false,
      "required": false
    },
    {
      "id": "937d8889-5a9e-4ea8-bddb-239e9979c5e5",
      "name": "Email",
      "type": "email",
      "type_config": {},
      "date_created": "1682970188205",
      "hide_from_guests": false,
      "required": false
    },
    {
      "id": "4bd4deaa-fbc8-4086-85ca-f0c803a34a4e",
      "name": "LS Email",
      "type": "email",
      "type_config": {},
      "date_created": "1683321494742",
      "hide_from_guests": false,
      "required": false
    }
  ],
  "dependencies": [],
  "linked_tasks": [],
  "locations": [],
  "team_id": "9010099710",
  "url": "https://app.clickup.com/t/868fm5fyq",
  "sharing": {
    "public": false,
    "public_share_expires_on": null,
    "public_fields": [
      "assignees",
      "priority",
      "due_date",
      "content",
      "comments",
      "attachments",
      "customFields",
      "subtasks",
      "tags",
      "checklists",
      "coverimage"
    ],
    "token": null,
    "seo_optimized": false
  },
  "permission_level": "create",
  "list": {
    "id": "901102682453",
    "name": "ClientList",
    "access": true
  },
  "project": {
    "id": "90111415391",
    "name": "CASES",
    "hidden": false,
    "access": true
  },
  "folder": {
    "id": "90111415391",
    "name": "CASES",
    "hidden": false,
    "access": true
  },
  "space": {
    "id": "90100237037"
  }
}