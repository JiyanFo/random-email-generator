import names
import random
from multiprocessing import Pool as ProcessPool
from tqdm import tqdm

n_processes = 150
name_list = []
domains = []
emails = []
n_emails = input("[+] Enter Number Of Emails To Generate : ")

# generation random names


def generateName():
    n_names = 0
    print("Generate Random Names")
    while (n_names < int(n_emails)):
        name = names.get_full_name()
        name_list.append(name)
        n_names += 1

# adds domains from .txt file to domain list


def generateDomainList():
    with open("r_domains.txt", "r") as provider:
        for domain in provider:
            domains.append(domain)

# generate e-mails from random names and domains


def generateMailList():
    generator = (3 * n for n in range(len(name_list)))
    for n in tqdm(generator, total=len(name_list), desc="Generate Random Emails"):
        for name in name_list:
            email = name.lower().replace(" ", ".") + "@" + random.choice(domains)
            emails.append(email)
            # print(email)


def save_to_file():
    with open("emails.txt", "wt", encoding="utf-8") as file:
        file.write(''.join(emails))


if __name__ == "__main__":
    generateName()
    generateDomainList()
    generateMailList()
    save_to_file()
print("DONE!")
