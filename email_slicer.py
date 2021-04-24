email=input("Enter your email id: ").strip()
username=email[:email.index("@")]
domain_name=email[email.index("@")+1:]

print(f"Your username is {username} and domain name is {domain_name}")