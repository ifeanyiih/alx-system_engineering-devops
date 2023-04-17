# 0x13. Firewall
Block all incoming traffic but the following TCP ports:
-	22 (SSH)
-	443 (HTTPS SSL)
-	80 (HTTP)
Installing ufw firewall and setup rules on our servers.


## Task 100-port_forwarding
This enables the forwarding of traffic on port 8080/tcp to port 80/tcp

First edit the file /etc/ufw/sysctl.conf, setting the following:

		net/ipv4/ip_forward=1
Then add the following intructions to the /etc/ufw/before.rules file:

	*nat
	:PREROUTING ACCEPT [0:0]
	-A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 500
	COMMIT

### Resource
[www.baeldung.com](https://www.baeldung.com/linux/ufw-port-forward) - The
information here was very helpful in completion of this task.
