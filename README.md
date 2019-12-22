# Windows10-Compat-Scan
Windows 10 Compat Scan is a tool used at work to check for Windows 7 machines that are eligible for Windows 10 upgrade.
### Steps in order to use this.
1. Download [7zip](https://www.7-zip.org/download.html)
2.Download and extract Windows 10 ISO (32bit and 64bit) into a folder called Win1064 and Win1032 respectively.
⋅⋅*[Go here and follow step 4](https://windowsreport.com/windows-10-iso-file-not-downloading/)
2. Once it's been extracted, right-click the respected folders, and select 7zip --> Add to archive... --> Archive format --> zip
3. Open your browser and upload the files to your Google Drive
4. Create a shareable link of the zip files. Make sure set the settings of the zip files is set to public or sharable to those who has the link.
5. Copy the ID of the file and paste it to the respected section of the code. i.e. get the sharable link ID of the 32 bit zip and paste it on the corresponding code. Same goes with 64 bit.
6. Run the CompatScan.py and this would return an output on the terminal or cmd
