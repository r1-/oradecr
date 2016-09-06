# oradecr
decrypt Oracle passwords with challenge/response and password hashes

oradec11 decrypts password hashes for Oracle 11.1 and 11.2. Based on Laslo Toth tool (http://www.soonerorlater.hu/index.khtml?article_id=512 - no more available)

oradec12 decrypts password hashes for Oracle12

Challenge response can be obtained by network sniffing : Server's and client's AUTH_SESSKEY and client's AUTH_PASSWORD 

Password hashes are stored in the database :
select spare4 from sys.user$;

The "S" part is needed for oradec11 

The "T" part is needed for oradec12

## Example Oracle 11g

SQL> select spare4 from sys.user$ where name='DBSNMP';

**S:73262299D1E5097AA2B9C4C49673F8E6DE29D1FA69C2FEF3877294A08221**


## Example Oracle 12c
SQL> select spare4 from sys.user$ where name='DBSNMP';

S:10E9A35C13D222FF83335EDDF304DC1DBDC73A6CAA60F930FC9B7CC3D2FD;H:ABBCDC5CD291503
88884FA4D59ABADD6;**T:09996F7FA5F5782F3C0D496E0219EB740A5A51C380907F8BB0238FBA0B56
2B4BD05F27CA102EA28A3EF9EDD09AA334E29E9E1C5E50B3EAE586DC78E918D53C9FA49534C6D73F
3BBA3D33837F343A7165**
