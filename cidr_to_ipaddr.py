from operator import index
import netaddr
import ipaddress


def cidr_to_numberof_ipaddr(cidr):
    ip, cidr_sz = cidr.split('/')
    # print(f"ip={ip}, cidr_sz= {cidr_sz}")
    return 2 ** (32 - int(cidr_sz))


def cidr_to_ipaddr_list(cidr):
    ip, cidr_sz = cidr.split('/')
    iplist = []
    # print(f"ip={ip}, cidr_sz= {cidr_sz}")
    numbr_of_ip = 2 ** (32 - int(cidr_sz))

    for cnt in range(numbr_of_ip):
        ip_index = ip.rindex(".")
        iplist.append(ip[:ip_index]+"."+str(cnt))
    return iplist


def ipaddr_to_cidr(startip, endip):
    # octet1*2^24 + octet2*2^16 + octet3*2^8 + octet4
    ip1_list = startip.split(".", 4)
    ip2_list = endip.split(".", 4)
    ip1_int = int(ip1_list[0]) * (2**24) + int(ip1_list[1]) * \
        (2**16) + int(ip1_list[2]) * (2**8) + int(ip1_list[3])
    ip2_int = int(ip2_list[0]) * (2**24) + int(ip2_list[1]) * \
        (2**16) + int(ip2_list[2]) * (2**8) + int(ip2_list[3])
    numbr_of_ip = ip2_int - ip1_int
    numbr_of_ip = 2 ** (32 - int(cidr_sz))
    # import netaddr
    # cidrs = netaddr.iprange_to_cidrs(startip, endip)


print("TotalIP=", cidr_to_numberof_ipaddr("10.0.0.0/26"))
iplist = cidr_to_ipaddr_list("10.0.0.0/26")
print("List=", iplist)
print(
    f"ip-Start={iplist[0]} , ip-End={iplist[len(iplist)-1]}")

print(ipaddr_to_cidr("10.0.0.0", "10.0.0.63"))
