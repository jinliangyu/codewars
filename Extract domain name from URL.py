# 5 kyu
# Extract the domain name from a URL
"""
Write a function that when given a URL as a string, parses out
just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""
# clever method
"""
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
"""


def domain_name(url):
    alist = url.split('//')
    blist = alist[-1].split('www.')
    # print blist
    clist = blist[-1].split('.com')
    d = clist[0].split('.')
    return d[0]

print domain_name("http://github.com/carbonfive/raygun")
print domain_name("http://www.zombie-bites.com")
print domain_name("https://www.cnet.com")
