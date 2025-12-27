#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    # Check for empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # List of placeholders to replace
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        result = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            result = result.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"

        # Write the output file
        try:
            with open(filename, "w") as file:
                file.write(result)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
