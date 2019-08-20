from string import Template

def main():
    str1 = "You are watching {0} by {1}".format("Advance Python", "Peter Martin")
    print(str1)

    # Define a template string
    templ = Template("You are watching ${title} by ${author}")

    # Use substitute method to provide values to template
    str2 = templ.substitute(title="Advance Python", author="Peter Martin")
    print(str2)

    # Use substitute method with dictionary
    data = {
        "title": "Advance Python",
        "author": "Peter Martin"
    }
    str3 = templ.substitute(data)
    print(str3)




main()