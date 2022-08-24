import os
import sys


  
def display_usage():
    print('''
          To run the script use the following command
          python3 dnbackup.py local_dir remote_dir file_types_to_exclude
          eg
          python3 dnbackup.py username host /home/username/dir1 /serverhome/username/dir1 .mp3 .amr


          python dnbackup.py dawahnig 185.164.35.20 /public_html/scripts/python/v24_test_backup D:/v24_run_backup/ .mp3 .amr

          python dnbackup.py dawahnig 185.164.35.20 C: /public_html/scripts/python/v24_test_backup .mp3 .amr

          rsync -a dawahnig@185.164.35.20:/public_html/scripts/python/v24_test_backup /v24_run_backup/ 
          rsync -a username@remote_host:/home/username/dir1 place_to_sync_on_local_machine
          rsync -a dawahnig@mediaserver:~/public_html/scripts/python/v24_test_backup dawahnig@185.164.35.20:/../v24_run_backup/ 
          dawahnig@mediaserver:~/public_html/scripts/python

            Usage: rsync [OPTION]... SRC [SRC]... DEST
                or   rsync [OPTION]... SRC [SRC]... [USER@]HOST:DEST
                or   rsync [OPTION]... SRC [SRC]... [USER@]HOST::DEST
                or   rsync [OPTION]... SRC [SRC]... rsync://[USER@]HOST[:PORT]/DEST
                or   rsync [OPTION]... [USER@]HOST:SRC [DEST]
                or   rsync [OPTION]... [USER@]HOST::SRC [DEST]
                or   rsync [OPTION]... rsync://[USER@]HOST[:PORT]/SRC [DEST]

                rsync -av C:\Users\fyunu\OneDrive\Desktop dawahnig@185.164.35.20:/public_html/scripts/python/v24_test_backup

            # username: dawahnig
            # host: 185.164.35.20
            # local_dir: D:/v24_run_backup/ 
            # remote_dir: /public_html/scripts/python/v24_test_backup
            # file_types_to_exclude: .mp3 .amr
          ''')


def pasrse_arguments() -> list:
    if len(sys.argv) < 5:
        display_usage()
        exit(1)

    username = sys.argv[1]
    host = sys.argv[2]
    local = sys.argv[3]
    remote = sys.argv[4]
    excluded_file_extentions = sys.argv[5:] if len(sys.argv) > 5 else None
    return [username, host, remote, local, excluded_file_extentions]


def format_file_extensions(extensions: list) -> set:
    if not extensions:
        return set()
    file_ext = list(map(lambda extension: extension.strip('.'), extensions))
    file_ext = list(map(lambda extension: '*.' + extension, file_ext))
    return file_ext


def backup_files(local_directory, remote_directory, username, host, file_ext):
    # cmd = f"rsync -av {username}@{host}:{remote_directory + '/*'} {local_directory} --progress --exclude '{set(file_ext)}'"
    cmd = f"rsync -av {username}@{host}:{remote_directory + '/*'} {local_directory} --progress --exclude '{set(file_ext)}'"
    print(f'\nNow Attempting to backup files/folders in {remote_directory} to {local_directory}\nInput your password in the next prompt\n')
    os.system(cmd)


if __name__ == '__main__':
    username, host, local_dir, remote_dir, excluded_file_extentions = pasrse_arguments()
    formated_extension = format_file_extensions(excluded_file_extentions)
    backup_files(local_dir, remote_dir, username, host, formated_extension)
    print('\n\nDone ..........................\n\n')
