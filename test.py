import json
import re

with open("results.json", "r") as f:
    data = json.load(f)

result_history = []
count = 1
for message in data:
    result = {}
    message = message["content"]
    lines = message.split("\n")
    team1_members = []
    team2_members = []
    result["map"] = lines[4]
    result["team1_name"] = lines[6].split(" ")[1]
    result["team2_name"] = lines[8].split(" ")[1]
    for idx, line in enumerate(lines[7:]):
        if line == '':

            break
        else:
            team1_members.append(line)

    result["team1_members"] = lines[6].split(" ")







# def parse_message(message_str):
#     # Use a regular expression to extract the winner or tie status
#     result = re.search(r"(Team [\w\s]+)(?: ties | beats )(Team [\w\s]+)", message_str)
#     if result:
#         winner = result.group(1)
#         loser = result.group(2)
#     else:
#         winner = "Tie"
#         loser = "Tie"

#     # Use a regular expression to extract the team names and members
#     team_pattern = r"(Team [\w\s]+)(?:\([\w\s-]+\))\n((?:[\w\s]+\n)+)(Team [\w\s]+)(?:\([\w\s-]+\))\n((?:[\w\s]+\n)+)"
#     teams = re.search(team_pattern, message_str)
#     print(teams)
#     team1_name = teams.group(1)
#     team1_members = teams.group(2).split()
#     team2_name = teams.group(3)
#     team2_members = teams.group(5).split()

#     # Return the extracted information as a dictionary
#     return {
#         "winner": winner,
#         "loser": loser,
#         "team1_name": team1_name,
#         "team1_members": team1_members,
#         "team2_name": team2_name,
#         "team2_members": team2_members
#     }

# parse_message(message)