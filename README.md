# heliumtosmstools
Convert an Android SMS backup database created by [Helium Backup](https://www.clockworkmod.com/carbon) into the format used by [smstools](https://github.com/t413/SMS-Tools)

I purchased Helium Backup as a solution to my Android backup needs several years ago when I got a new phone. I recently decided to do a factory reset on an ailing device, and while I was at it, upgrade from stock Android 5.1 to Cyanogenomd 13 (based on Android 6.0). I used Helium without thinking, and was able to successfully restore everything except my SMS messages after installing CM. Frustrated, I began to look for another way to restore my backup.

The final solution was this:
- Ensure you have a backup of /data/data/com.android.providers.telephony/databases/mmssms.db. You might need to push it back into that location on your device should something go wrong. (The first pass of this tool inverted my sent/received messages, which was undesirable.)
- Use my homemade tool to convert a sanitized version of the backed up com.android.providers.telephony.ab file. Sanitization should include stripping out the file header at the beginning and the call logs at the end so your input file is simply an array of json objects representing SMS messages.
- Run the converted file through smstools to create an XML file for [SMS Backup and Restore](http://www.carbonite.com/en/apps/call-log-sms-backup-restore).
- Restore the XML file using SMS Backup and Restore.