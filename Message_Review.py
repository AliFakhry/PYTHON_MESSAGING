def init_message(number, carrier, name, company):
    message_1 = f"Hello {name},\n"
    message_2 = f"Thank you for doing your business with {company}!\n"
    message_3 = f"If possible, could you please tell us what you though about our service?\n"
    message_4 = f"We appreciate your feedback."
    t_message = message_1 + message_2 + message_3 + message_4
    return t_message

def pos_message(number, carrier, name, company):
    mobile_link = company(company, "mobile")
    desktop_link = company(company, "desktop")
    message_1 = f"Hello {name},\n"
    message_2 = f"Thank you for well regards!\n"
    message_3 = f"If you do not mind, could you please take the time to write a review on Google?\n"
    message_4 = f"We would really appreciate it\n."
    message_5 = f"Mobile link: \n."
    message_6 = f"{mobile_link}\n."
    message_6 = f"Desktop link: \n."
    message_7 = f"{desktop_link}\n."
    message_8 = f"\nPlease keep in mind that you need a Google account to post a review."
    t_message = message_1 + message_2 + message_3 + message_4 + message_5 + message_6 + message_7 + message_8
    return t_message

def company_review(company, version):
    if company == "WCE":
        if version == "mobile":
            return "http://shorturl.at/hjnIM"
        return "https://shorturl.at/szCNT"
    