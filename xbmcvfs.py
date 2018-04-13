# coding: utf-8
# This file is generated from Kodi source code and post-edited
# to correct code style and docstrings formatting.
# License: GPL v.3 <https://www.gnu.org/licenses/gpl-3.0.en.html>
"""
Virtual file system functions on Kodi

Offers classes and functions offers
acces to the Virtual File Server (VFS) which you can use to manipulate files
and folders.
"""
from typing import Union, List, Tuple

__kodistubs__ = True

int_type = Union[int, long]
str_type = Union[str, unicode]


class File(object):
    """
    Kodi's file class

    ``xbmcvfs.File(filepath, [mode])``

    :param filepath: string Selected file path 
    :param mode: [opt] string Additional mode options (if no mode is supplied,
        the default is Open for Read).

    =====  ===============
    Mode   Description    
    =====  ===============
    w      Open for write 
    =====  ===============

    **Example:**

    .. code-block:: python

        ..
        f = xbmcvfs.File(file, 'w')
        ..
    """
    
    def __init__(self, filepath, mode=None):
        # type: (str_type, str) -> None
        pass
    
    def read(self, numBytes=0):
        # type: (int_type) -> str
        """
        ``read([bytes])`` 

        Read file parts as string. 

        :param bytes: [opt] How many bytes to read - if not set it will read
            the whole file
        :return: string

        **Example:**

        .. code-block:: python

            ..
            f = xbmcvfs.File(file)
            b = f.read()
            f.close()
            ..
        """
        return ""
    
    def readBytes(self, numBytes=0):
        # type: (int_type) -> bytearray
        """
        ``readBytes(numbytes)`` 

        Read bytes from file. 

        :param numbytes: How many bytes to read [opt]- if not set it will
            read the whole file
        :return: bytearray

        **Example:**

        .. code-block:: python

            ..
            f = xbmcvfs.File(file)
            b = f.read()
            f.close()
            ..
        """
        return bytearray()
    
    def write(self, buffer):
        # type: (Union[str, bytearray]) -> bool
        """
        ``write(buffer)`` 

        To write given data in file. 

        :param buffer: Buffer to write to file 
        :return: True on success.

        **Example:**

        .. code-block:: python

            ..
            f = xbmcvfs.File(file, 'w')
            result = f.write(buffer)
            f.close()
            ..
        """
        return True
    
    def size(self):
        # type: () -> long
        """
        ``size()`` 

        Get the file size. 

        :return: The file size

        **Example:**

        .. code-block:: python

            ..
            f = xbmcvfs.File(file)
            s = f.size()
            f.close()
            ..
        """
        return 0L
    
    def seek(self, seekBytes, iWhence):
        # type: (int_type, int) -> long
        """
        ``seek(seekBytes, iWhence)`` 

        Seek to position in file. 

        :param seekBytes: position in the file 
        :param iWhence: where in a file to seek from [0 begining, 1 current ,
            2 end possition]

        **Example:**

        .. code-block:: python

            ..
            f = xbmcvfs.File(file)
            result = f.seek(8129, 0)
            f.close()
            ..
        """
        return 0L
    
    def close(self):
        # type: () -> None
        """
        ``close()`` 

        Close opened file. 



        **Example:**

        .. code-block:: python

            ..
            f = xbmcvfs.File(file)
            f.close()
            ..
        """
        pass
    

class Stat(object):
    """
    Get file or file system status

    ``xbmcvfs.Stat(path)``

    These class return information about a file. Execute (search) permission
    is required on all of the directories in path that lead to the file.

    :param path: [string] file or folder

    New function added

    **Example:**

    .. code-block:: python

        ..
          st = xbmcvfs.Stat(path)
          modified = st.st_mtime()
        ..
    """
    
    def __init__(self, path):
        # type: (str_type) -> None
        pass
    
    def st_mode(self):
        # type: () -> long
        """
        ``st_mode()`` 

        To get file protection. 

        :return: st_mode 
        """
        return 0L
    
    def st_ino(self):
        # type: () -> long
        """
        ``st_ino()`` 

        To get inode number. 

        :return: st_ino 
        """
        return 0L
    
    def st_dev(self):
        # type: () -> long
        """
        ``st_dev()`` 

        To get ID of device containing file. 

        The st_dev field describes the device on which this file resides.

        :return: st_dev 
        """
        return 0L
    
    def st_nlink(self):
        # type: () -> long
        """
        ``st_nlink()`` 

        To get number of hard links. 

        :return: st_nlink 
        """
        return 0L
    
    def st_uid(self):
        # type: () -> long
        """
        ``st_uid()`` 

        To get user ID of owner. 

        :return: st_uid 
        """
        return 0L
    
    def st_gid(self):
        # type: () -> long
        """
        ``st_gid()`` 

        To get group ID of owner. 

        :return: st_gid 
        """
        return 0L
    
    def st_size(self):
        # type: () -> long
        """
        ``st_size()`` 

        To get total size, in bytes. 

        The st_size field gives the size of the file (if it is a regular file
        or a symbolic link) in bytes. The size of a symbolic link (only on Linux
        and Mac OS X) is the length of the pathname it contains, without
        a terminating null byte.

        :return: st_size 
        """
        return 0L
    
    def atime(self):
        # type: () -> long
        """
        ``atime()`` 

        To get time of last access. 

        :return: st_atime 
        """
        return 0L
    
    def mtime(self):
        # type: () -> long
        """
        ``mtime()`` 

        To get time of last modification. 

        :return: st_mtime 
        """
        return 0L
    
    def ctime(self):
        # type: () -> long
        """
        ``ctime()`` 

        To get time of last status change. 

        :return: st_ctime 
        """
        return 0L


def copy(strSource, strDestnation):
    # type: (str_type, str_type) -> bool
    """
    ``xbmcvfs.copy(source, destination)`` 

    Copy file to destination, returns true/false. 

    :param source: file to copy. 
    :param destination: destination file 
    :return: True if successed

    **Example:**

    .. code-block:: python

        ..
        success = xbmcvfs.copy(source, destination)
        ..
    """
    return True


def delete(file):
    # type: (str_type) -> bool
    """
    ``xbmcvfs.delete(file)`` 

    Delete a file

    :param file: File to delete 
    :return: True if successed

    **Example:**

    .. code-block:: python

        ..
        xbmcvfs.delete(file)
        ..
    """
    return True


def rename(file, newFile):
    # type: (str_type, str_type) -> bool
    """
    ``xbmcvfs.rename(file, newFileName)`` 

    Rename a file

    :param file: File to rename 
    :param newFileName: New filename, including the full path 
    :return: True if successed

    Moving files between different filesystem (eg. local to nfs://)
    is not possible on all platforms. You may have to do it manually by using
    the copy and deleteFile functions.

    **Example:**

    .. code-block:: python

        ..
        success = xbmcvfs.rename(file,newFileName)
        ..
    """
    return True


def exists(path):
    # type: (str_type) -> bool
    """
    ``xbmcvfs.exists(path)`` 

    Check for a file or folder existance

    :param path: File or folder (folder must end with slash or backslash) 
    :return: True if successed

    **Example:**

    .. code-block:: python

        ..
        success = xbmcvfs.exists(path)
        ..
    """
    return True


def mkdir(path):
    # type: (str_type) -> bool
    """
    ``xbmcvfs.mkdir(path)`` 

    Create a folder. 

    :param path: Folder to create 
    :return: True if successed

    **Example:**

    .. code-block:: python

        ..
        success = xbmcvfs.mkdir(path)
        ..
    """
    return True


def mkdirs(path):
    # type: (str_type) -> bool
    """
    ``xbmcvfs.mkdirs(path)`` 

    Make all directories along the path 

    Create folder(s) - it will create all folders in the path.

    :param path: Folders to create 
    :return: True if successed

    **Example:**

    .. code-block:: python

        ..
        success = xbmcvfs.mkdirs(path)
        ..
    """
    return True


def rmdir(path, force=False):
    # type: (str_type, bool) -> bool
    """
    ``xbmcvfs.rmdir(path)`` 

    Remove a folder. 

    :param path: Folder to remove 
    :return: True if successed

    **Example:**

    .. code-block:: python

        ..
        success = xbmcvfs.rmdir(path)
        ..
    """
    return True


def listdir(path):
    # type: (str_type) -> Tuple[List[str], List[str]]
    """
    ``xbmcvfs.listdir(path)`` 

    Lists content of a folder. 

    :param path: Folder to get list from 
    :return: Directory content list

    **Example:**

    .. code-block:: python

        ..
        dirs, files = xbmcvfs.listdir(path)
        ..
    """
    return [""], [""]
