# Windows10-Compat-Scan
Windows 10 Compat Scan is a tool used at work to check for Windows 7 machines that are eligible for Windows 10 upgrade. This is a very helpful tool for IT specially for those who are using RMM such as Atera. This tool is a huge time saver for both customer and IT support.This tool can be run in the background when using Atera's cmd tools. Ideally, this tool should be compiled to a 32bit exe using pyinstaller.
### Steps in order to use this.
1. Download [7zip](https://www.7-zip.org/download.html)
2.Download and extract Windows 10 ISO (32bit and 64bit) into a folder called Win1064 and Win1032 respectively.
⋅⋅*[Go here and follow step 4](https://windowsreport.com/windows-10-iso-file-not-downloading/)
3. Once it's been extracted, right-click the respected folders, and select 7zip --> Add to archive... --> Archive format --> zip
4. Open your browser and upload the files to your Google Drive
5. Create a shareable link of the zip files. Make sure set the settings of the zip files is set to public or sharable to those who has the link.
6. Copy the ID of the file and paste it to the respected section of the code. i.e. get the sharable link ID of the 32 bit zip and paste it on the corresponding code. Same goes with 64 bit.
7. Run the CompatScan.py and this would return an output on the terminal or cmd


# TODO: ### **Tool Revamp
- [ ] Enable the use of Internet Explorer
- [ ] If Chrome is not downloaded, allow for automatic installation of Chrome.
    - [ ] Check for installed Web Browsers
- [ ] Extract ISO on a Temp folder to access setup.exe
- [ ] Run the setup.exe with arguements in order for it be silently check if Windows 10 is compatible with the machine