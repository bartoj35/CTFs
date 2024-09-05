from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
import json

key = ECC . generate ( curve = 'p256' )
pubkey = key . public_key ( ) . export_key ( format = 'PEM' )

f = open ( 'pubkey', 'w' )
f . write ( pubkey )
f . close ( )

date = '1825717455'
h = SHA256 . new ( date . encode ( 'utf-8' ) )
signature = DSS . new ( key, 'fips-186-3' ) . sign ( h ) . hex ( )


f = open ( 'index.html', 'w' )
json . dump ( {
    'date': date,
    'signature': signature
}, f )
f . close ( )
