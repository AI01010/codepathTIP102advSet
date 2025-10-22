# gallery subdomain traffic
# count of domain visits
# split num and string by space
# split domian and subdomains by .
# assume max d1-3

def subdomain_visits(cpdomains):
    freq = {}

    for cpdomain in cpdomains:
        arr = cpdomain.split()
        vists = int(arr[0])
        domainArr = arr[1].split('.')
        
        for i in range(len(domainArr)):
            domainName = 
            freq[]