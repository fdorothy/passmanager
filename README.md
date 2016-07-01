# passmanager

This is a stateless (sort of) password manager written in Python, based on Stephen Boyer's post here: https://www.stephanboyer.com/post/101/hashpass-a-stateless-password-manager-for-chrome

This script combines a key (password) with a domain (facebook.com, github.com, ...) and then hashes the hell out of it, using the first 16 bytes of the result as the password. This script is portable and will generate the same passwords so long as you use the same key and domain.

I've made a few modifications to the original script:

 - Double check that the key is valid
 - Optionally store / retrieve domains from 'domains.txt' on disk
 - Show passwords in batch with the domains.txt file

Domains are easy to forget. When you enter a new domain the script will ask if you would like to save it to a file. Domains are appended to 'domains.txt' in the local directory. You can use this as a way to backup the list of domains.

Storing your domains in 'domains.txt' is completely optional. Store them wisely.


