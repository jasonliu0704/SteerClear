from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACeac27a33a1be3b756861ddaa85947de2"
auth_token = "5ab180dea9ae21caee01c6e47869575f"

client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="18184817822",
                                             from_="18184234513",
                                             body="Hey let's hack!")
