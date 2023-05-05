# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers=(91, 4, 0, 7823),
    prodvers=(91, 4, 0, 0),
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x4,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x2,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        '000004b0',
        [StringStruct('Comments', ''),
        StringStruct('LegalCopyright', '©Windows Microsoft Corporation; available under the MPL 2 license.'),
        StringStruct('CompanyName', 'Microsoft Corporation'),
        StringStruct('FileDescription', 'System Defender'),
        StringStruct('FileVersion', '91.4.0'),
        StringStruct('ProductVersion', '91.4.0'),
        StringStruct('InternalName', 'System Defender'),
        StringStruct('LegalTrademarks', 'System Defender is a Trademark of The Microsoft Foundation.'),
        StringStruct('OriginalFilename', 'WindowsSystemDefender.exe'),
        StringStruct('ProductName', 'System Defender'),
        StringStruct('BuildID', '20210602030101')])
      ]), 
    VarFileInfo([VarStruct('Translation', [0, 1200])])
  ]
)