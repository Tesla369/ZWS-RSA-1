#-*- coding: utf-8 -*-

# Zero-width steganography
# Idea: use two different kinds of zero-width (invisible) spaces to embed a hidden message in text
# Hopefully after compression it will not have a much higher footprint in bytes

import base64
import click

HIDDEN_ZERO = u'​' # Zero-width space
HIDDEN_ONE = u'‍' # Zero-width non-joiner

def decode(string):
    return string.replace(HIDDEN_ZERO, '0').replace(HIDDEN_ONE, '1')

def encode(string):
    return string.replace('0', HIDDEN_ZERO).replace('1', HIDDEN_ONE)

def str2bin_viab16(string):
    return bin(int(base64.b16encode(string), 16))[2:]

def bin2str_viab16(binary):
    return base64.b16decode(
        "{:x}".format(int(binary, 2)).upper()
    )

def hide_message(secret):
    return encode(str2bin_viab16(secret))

def retrieve_hidden_message(body):
    secret_message = []

    for char in body.decode('utf-8'):
        if ord(char) in (ord(HIDDEN_ZERO), ord(HIDDEN_ONE)):
            secret_message.append(char)

    if secret_message:
        return bin2str_viab16(decode(''.join(secret_message)))


@click.command()
@click.option('--secret', '-s', type=click.File('rb'), help='Filename of the secret message')
@click.argument('plainsight', type=click.File('rb+'))
def cli(plainsight, secret):

    if secret:
        # If a secret exists, append it to the plainsight message
        secret_message = secret.read()
        plainsight_message = plainsight.read()
        plainsight.write(hide_message(secret_message).encode('utf-8'))

        click.echo('[OK] Message added to {0}'.format(plainsight))

    else:
        # If no secret exists, try to extract a hidden message from the plainsight message
        message = retrieve_hidden_message(plainsight.read())

        if message:
            click.echo('{0}'.format(message))
        else:
            click.echo('[OK] No hidden message found in this file.')


if __name__ == '__main__':
    cli()
#‍​​​‍‍​​‍​‍‍​‍​​‍​‍​‍​​​‍​‍‍​‍​​‍​​​​​​‍‍​​​‍‍​‍‍​‍‍‍‍​‍‍​​‍​​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍​​‍‍‍​​‍‍‍​‍​​​‍​​​​​​‍‍‍​‍​‍​‍‍‍​‍​​​‍‍​​‍‍​​​‍​‍‍​‍​​‍‍‍​​​​​‍​​​​​​​‍​‍‍​‍​​‍​‍​‍​​​‍​‍‍​‍​​​​‍​‍​​​​​‍​‍​​​‍​​​‍‍​​‍​​​​​​‍​‍‍​‍​​‍‍​​‍​‍​‍‍‍​​‍​​‍‍​‍‍‍‍​​‍​‍‍​‍​‍‍‍​‍‍‍​‍‍​‍​​‍​‍‍​​‍​​​‍‍‍​‍​​​‍‍​‍​​​​​‍​​​​​​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍​​‍​‍​‍‍​​‍‍‍​‍‍​​​​‍​‍‍​‍‍‍​​‍‍​‍‍‍‍​‍‍​​‍‍‍​‍‍‍​​‍​​‍‍​​​​‍​‍‍‍​​​​​‍‍​‍​​​​‍‍‍‍​​‍​​​​‍​‍​​​‍​​​‍‍​​‍​​​​​​‍​​‍​​‍​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​​​‍​​‍‍‍​‍​​​‍​​​​​​‍‍‍​‍​‍​‍‍‍​​‍‍​‍‍​​‍​‍​​‍​​​​​​‍‍‍​‍​​​‍‍‍​‍‍‍​‍‍​‍‍‍‍​​‍​​​​​​‍‍​​‍​​​‍‍​‍​​‍​‍‍​​‍‍​​‍‍​​‍‍​​‍‍​​‍​‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍​‍‍‍​​‍‍‍​‍​​​​‍​​​​​​‍‍​‍​‍‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍​​‍​​​‍‍‍​​‍‍​​‍​​​​​​‍‍​‍‍‍‍​‍‍​​‍‍​​​‍​​​​​​‍‍‍‍​‍​​‍‍​​‍​‍​‍‍‍​​‍​​‍‍​‍‍‍‍​​‍​‍‍​‍​‍‍‍​‍‍‍​‍‍​‍​​‍​‍‍​​‍​​​‍‍‍​‍​​​‍‍​‍​​​​​‍​​​​​​​‍​‍​​​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​‍‍​​‍‍​‍​​‍​‍‍‍​​‍‍​‍‍​‍​​‍​‍‍​​​‍​​‍‍​‍‍​​​‍‍​​‍​‍​​‍​‍​​‍​​‍​​​​​​‍‍‍​​‍‍​‍‍‍​​​​​‍‍​​​​‍​‍‍​​​‍‍​‍‍​​‍​‍​‍‍‍​​‍‍​​‍​​​​​​‍‍‍​‍​​​‍‍​‍‍‍‍​​‍​​​​​​‍‍​​‍​‍​‍‍​‍‍​‍​‍‍​​​‍​​‍‍​​‍​‍​‍‍​​‍​​​​‍​​​​​​‍‍​​​​‍​​‍​​​​​​‍‍​‍​​​​‍‍​‍​​‍​‍‍​​‍​​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​‍‍‍​​​‍​​​​​​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​​​​​​‍‍​‍​​‍​‍‍​‍‍‍​​​‍​​​​​​‍‍‍​‍​​​‍‍​​‍​‍​‍‍‍‍​​​​‍‍‍​‍​​​​​​‍​‍​​​‍​​​‍‍​​‍​​​​​​‍​​‍​​​​‍‍​‍‍‍‍​‍‍‍​​​​​‍‍​​‍​‍​‍‍​​‍‍​​‍‍‍​‍​‍​‍‍​‍‍​​​‍‍​‍‍​​​‍‍‍‍​​‍​​‍​​​​​​‍‍​​​​‍​‍‍​​‍‍​​‍‍‍​‍​​​‍‍​​‍​‍​‍‍‍​​‍​​​‍​​​​​​‍‍​​​‍‍​‍‍​‍‍‍‍​‍‍​‍‍​‍​‍‍‍​​​​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​‍​​‍​‍‍​‍‍‍‍​‍‍​‍‍‍​​​‍​​​​​​‍‍​‍​​‍​‍‍‍​‍​​​​‍​​​​​​‍‍‍​‍‍‍​‍‍​‍​​‍​‍‍​‍‍​​​‍‍​‍‍​​​​‍​​​​​​‍‍​‍‍‍​​‍‍​‍‍‍‍​‍‍‍​‍​​​​‍​​​​​​‍‍​‍​​​​‍‍​​​​‍​‍‍‍​‍‍​​‍‍​​‍​‍​​‍​​​​​​‍‍​​​​‍​​‍​​​​​​‍‍​‍‍​‍​‍‍‍​‍​‍​‍‍​​​‍‍​‍‍​‍​​​​​‍​​​​​​‍‍​‍​​​​‍‍​‍​​‍​‍‍​​‍‍‍​‍‍​‍​​​​‍‍​​‍​‍​‍‍‍​​‍​​​‍​​​​​​‍‍​​‍‍​​‍‍​‍‍‍‍​‍‍​‍‍‍‍​‍‍‍​‍​​​‍‍‍​​​​​‍‍‍​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​‍​​​​‍​​​​​​‍‍​‍​​‍​‍‍​‍‍‍​​​‍​​​​​​‍‍​​​‍​​‍‍‍‍​​‍​‍‍‍​‍​​​‍‍​​‍​‍​‍‍‍​​‍‍​​​​‍​‍​​​​​‍​‍​​‍‍​‍​​‍​‍‍​‍‍​‍​‍‍‍​​​​​‍‍​‍‍‍‍​‍‍‍​​‍​​‍‍‍​‍​​​​‍​​​​​​‍‍​​​‍​​‍‍​​​​‍​‍‍‍​​‍‍​‍‍​​‍​‍​​‍‍​‍‍​​​‍‍​‍​​​​​​‍​‍​​‍‍​‍​​‍​‍‍​‍‍​‍​‍‍‍​​​​​‍‍​‍‍‍‍​‍‍‍​​‍​​‍‍‍​‍​​​​‍​​​​​​‍‍​​​‍‍​‍‍​‍‍​​​‍‍​‍​​‍​‍‍​​​‍‍​‍‍​‍​‍‍​​​​‍​‍​​​​​‍​‍​​‍​​‍​​​​‍​​‍​​‍​‍​​​‍​​​‍​​​‍​​​‍​​​‍​‍​‍​​‍‍‍​​‍​‍‍‍‍‍​‍​‍‍​‍​​‍​​​‍​‍​‍​‍​​‍​​‍​​‍‍‍‍​​‍​​​​​​​‍‍‍‍​‍​​‍​​​​​​‍‍‍​‍​‍​​‍​​‍‍‍‍‍‍​​​‍​‍​​​​​​​‍​​​‍​‍‍​​‍​​‍‍‍​​‍​​​​​​​‍​​​‍‍​​‍​​​​​​‍​‍‍​‍​​‍‍​​‍​‍​‍‍‍​​‍​​‍‍​‍‍‍‍​​‍​‍‍​‍​‍‍‍​‍‍‍​‍‍​‍​​‍​‍‍​​‍​​​‍‍‍​‍​​​‍‍​‍​​​​​‍​​​​​​‍‍‍​​‍‍​‍‍‍​​​​​‍‍​​​​‍​‍‍​​​‍‍​‍‍​​‍​‍​​​​‍​‍​​‍​​‍​​​​‍​​‍​​‍​‍​​​‍​​​‍​​​‍​​​‍​​​‍​‍​‍​​‍‍‍​​‍​‍‍‍‍‍​‍​​‍‍‍‍​‍​​‍‍‍​​‍​​​‍​‍​​‍​​​​​​​‍‍‍‍​‍​​‍​​​​​​‍‍‍​‍​‍​​‍​​‍‍‍‍‍‍​​​‍​‍​​​​​​​‍​​​‍‍​‍​​‍​​‍‍‍​​‍​​​​​​​‍​​​‍‍​​‍​​​​​​‍​‍‍​‍​​‍‍​​‍​‍​‍‍‍​​‍​​‍‍​‍‍‍‍​​‍​‍‍​‍​‍‍‍​‍‍‍​‍‍​‍​​‍​‍‍​​‍​​​‍‍‍​‍​​​‍‍​‍​​​​​‍​​​​​​‍‍​‍‍‍​​‍‍​‍‍‍‍​‍‍​‍‍‍​​​‍​‍‍​‍​‍‍​‍​‍​​‍‍​‍‍‍‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍​​‍​‍​‍‍‍​​‍​​​​​‍​‍​​​​​‍​‍​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​‍‍​​​‍​​​​​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​​‍‍​‍‍​‍‍‍‍​‍‍​​‍​​​‍‍​​‍​‍​​‍​‍​​​​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍​​‍‍‍​​‍​‍​​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍‍‍​‍​‍​‍‍‍​​‍​​‍‍​‍‍‍​​​‍​​​​​​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍​​‍‍‍​​‍​‍‍‍​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​​​‍‍​‍‍​​‍​‍​​‍​‍​​​​‍​​‍​​​​‍​​‍​​‍​‍​​​‍​​​‍​​​‍​​​‍​​​‍​‍​‍​​‍‍‍​​‍​‍‍‍‍‍​‍​‍‍​‍​​‍​​​‍​‍​‍​‍​​‍​​‍​​‍‍‍‍​​‍​‍‍​​​​‍​​​​​​​‍​​‍‍‍​​‍‍​​​​​​‍​​‍‍‍​​‍​‍​​‍​​‍​‍‍‍​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​​​‍‍​‍‍​​‍​‍​​‍​‍​​​​‍​​‍​​​​‍​​‍​​‍​‍​​​‍​​​‍​​​‍​​​‍​​​‍​‍​‍​​‍‍‍​​‍​‍‍‍‍‍​‍​​‍‍‍‍​‍​​‍‍‍​​‍​​​‍​‍​​‍​‍‍​​​​‍​​​​​​​‍​​‍‍‍​​‍‍​​​‍​​‍​​‍‍‍​​‍​‍​​‍​​​​‍​‍​​​​​‍​‍​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​‍‍​​​‍​​​​​​‍‍​​‍​‍​‍‍​‍‍‍​​‍‍​​​‍‍​‍‍​‍‍‍‍​‍‍​​‍​​​‍‍​​‍​‍​​‍​‍​​​​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍​​‍‍‍​​‍​‍​​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍‍‍​‍​‍​‍‍‍​​‍​​‍‍​‍‍‍​​​‍​​​​​​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍​​‍‍‍​​‍​‍‍‍​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​​​‍‍​‍‍​​‍​‍​​‍​‍​​​​​‍​​‍‍‍​​‍‍​​​​​​‍​​‍‍‍​​‍​‍‍​​​​‍​​​​​​‍​​‍​​​​‍​​‍​​‍​‍​​​‍​​​‍​​​‍​​​‍​​​‍​‍​‍​​‍‍‍​​‍​‍‍‍‍‍​‍​‍‍​‍​​‍​​​‍​‍​‍​‍​​‍​​‍​​‍‍‍‍​​‍​‍​​‍​​‍​‍‍‍​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​​​‍‍​‍‍​​‍​‍​​‍​‍​​​​​‍​​‍‍‍​​‍‍​​​‍​​‍​​‍‍‍​​‍​‍‍​​​​‍​​​​​​‍​​‍​​​​‍​​‍​​‍​‍​​​‍​​​‍​​​‍​​​‍​​​‍​‍​‍​​‍‍‍​​‍​‍‍‍‍‍​‍​​‍‍‍‍​‍​​‍‍‍​​‍​​​‍​‍​​‍​‍​​‍​​​​‍​‍​​​​​‍​‍​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​‍‍​​​‍​​​​​​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍​​​‍‍​​‍​​‍‍​​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​‍​‍‍‍‍‍​‍‍‍​‍‍​​‍‍​‍​​‍​‍‍​​​​‍​‍‍​​​‍​​​‍‍​​​‍​​‍‍​‍‍​​​‍​‍​​​​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍​​‍‍‍​​‍​‍​​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍‍‍​‍​‍​‍‍‍​​‍​​‍‍​‍‍‍​​​‍​​​​​​‍‍​​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​​‍​‍​​​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​‍​​​​‍​‍​​​​‍‍​​​‍​​‍‍​​​​‍​‍‍‍​​‍‍​‍‍​​‍​‍​​‍‍​‍‍​​​‍‍​‍​​​​‍​‍‍‍​​‍‍​​​‍​​​‍‍​​​‍​​‍‍​‍‍​​‍‍​​‍​‍​‍‍​‍‍‍​​‍‍​​​‍‍​‍‍​‍‍‍‍​‍‍​​‍​​​‍‍​​‍​‍​​‍​‍​​​​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍​​‍‍‍​​‍​‍​​‍​​‍​‍‍​​​​‍​​​​​​​‍‍​​​‍​​‍‍​‍‍​​​‍​‍​​‍​​‍​‍​​‍​‍​‍‍​‍‍​​‍‍​​‍​​​‍‍‍​‍​​‍​‍‍‍​‍​​​​‍​‍​​​​​‍​‍​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​‍‍​​​‍​​​​​​‍‍​​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​​‍‍​​‍​​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍​​‍​‍‍‍‍‍​‍‍‍​‍‍​​‍‍​‍​​‍​‍‍​​​​‍​‍‍​​​‍​​​‍‍​​​‍​​‍‍​‍‍​​​‍​‍​​​​‍‍​​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍​​​​‍​‍‍‍​​‍​​‍‍‍‍​​‍​​‍​‍​​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍‍‍​‍​‍​‍‍‍​​‍​​‍‍​‍‍‍​​​‍​​​​​​‍‍​​​‍​​‍‍​​​​‍​‍‍‍​​‍‍​‍‍​​‍​‍​​‍‍​‍‍​​​‍‍​‍​​​​‍​‍‍‍​​‍‍​​​‍​​​‍‍​​​‍​​‍‍​‍‍​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​​‍‍​‍‍​‍‍‍‍​‍‍​​‍​​​‍‍​​‍​‍​​‍​‍​​​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​‍​​‍‍‍‍​‍‍​​‍‍‍​‍​​‍‍‍‍​​​​‍‍‍‍‍​‍​​‍​​​‍​​​‍​‍‍‍​​‍‍​​‍‍​​‍‍​‍‍‍‍​‍‍‍​​‍​​‍‍​‍‍​‍​‍‍​​​​‍​‍‍‍​‍​​​​‍​‍​​​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​‍​​​​‍​‍​​​​‍‍​​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍​​​​‍​‍‍‍​​‍​​‍‍‍‍​​‍​​‍​‍‍​​​​‍​​​​​​​‍‍​​‍​​​‍​‍​​‍​​‍​‍​​‍​​‍​‍‍‍​​‍‍‍​‍​‍​‍‍‍​​​​​‍‍‍​​​​​‍‍​​‍​‍​‍‍‍​​‍​​​‍​‍​​​​​‍​‍​​‍​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​‍​​‍​​​​‍​‍​​​​​‍​‍​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​‍‍​​​‍​​​​​​‍‍​‍​​​​‍‍​‍​​‍​‍‍​​‍​​​‍‍​​‍​‍​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​‍​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​​‍​‍​​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍‍‍​‍​‍​‍‍‍​​‍​​‍‍​‍‍‍​​​‍​​​​​​‍‍​​‍​‍​‍‍​‍‍‍​​‍‍​​​‍‍​‍‍​‍‍‍‍​‍‍​​‍​​​‍‍​​‍​‍​​‍​‍​​​​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍​​​‍‍​​‍​​‍‍​​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​‍​‍‍‍‍‍​‍‍‍​‍‍​​‍‍​‍​​‍​‍‍​​​​‍​‍‍​​​‍​​​‍‍​​​‍​​‍‍​‍‍​​​‍​‍​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​​‍​‍​​‍​​‍​‍​​‍​​​​‍​‍​​​​​‍​‍​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​‍‍​​​‍​​​​​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍‍‍​​‍​​‍‍​‍​​‍​‍‍​​‍​‍​‍‍‍​‍‍​​‍‍​​‍​‍​‍​‍‍‍‍‍​‍‍​‍​​​​‍‍​‍​​‍​‍‍​​‍​​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​‍‍‍​​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​‍​​​​‍‍​​​‍​​‍‍​‍‍‍‍​‍‍​​‍​​​‍‍‍‍​​‍​​‍​‍​​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​​​​​​​‍‍‍‍​‍​​‍​​​​​​‍​‍‍​‍‍​‍​‍‍‍​‍​​​​‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​​‍‍​​‍‍​‍‍‍‍​‍‍‍​​‍​​​‍​​​​​​‍‍​​​‍‍​‍‍​‍​​​​‍‍​​​​‍​‍‍‍​​‍​​​‍​​​​​​‍‍​‍​​‍​‍‍​‍‍‍​​​‍​​​​​​‍‍​​​‍​​‍‍​‍‍‍‍​‍‍​​‍​​​‍‍‍‍​​‍​​‍​‍‍‍​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​​‍‍​‍‍​‍‍‍‍​‍‍​​‍​​​‍‍​​‍​‍​​‍​‍​​​​​‍​​‍‍‍​‍‍‍​‍​‍​‍‍‍​‍​​​‍‍​​‍‍​​​‍​‍‍​‍​​‍‍‍​​​​​‍​​‍‍‍​​‍​‍​​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​‍​​‍​‍‍​​‍‍​​​‍​​​​​​‍‍​‍‍‍‍​‍‍‍​​‍​​‍‍​​‍​​​​‍​‍​​​​‍‍​​​‍‍​‍‍​‍​​​​‍‍​​​​‍​‍‍‍​​‍​​​‍​‍​​‍​​‍​​​​​​‍‍​‍​​‍​‍‍​‍‍‍​​​‍​​​​​​​‍​‍​​​​‍‍​‍‍‍‍​‍‍‍​​‍​​‍‍​​‍​​​​‍​‍​​​​‍​​‍​​​​‍​​‍​​‍​‍​​​‍​​​‍​​​‍​​​‍​​​‍​‍​‍​​‍‍‍​​‍​‍‍‍‍‍​‍​‍‍​‍​​‍​​​‍​‍​‍​‍​​‍​​‍​​‍‍‍‍​​‍​‍​​‍​​‍​‍‍​​​​‍​​​​​​‍‍​‍‍‍‍​‍‍‍​​‍​​‍‍​​‍​​​​‍​‍​​​​‍​​‍​​​​‍​​‍​​‍​‍​​​‍​​​‍​​​‍​​​‍​​​‍​‍​‍​​‍‍‍​​‍​‍‍‍‍‍​‍​​‍‍‍‍​‍​​‍‍‍​​‍​​​‍​‍​​‍​‍​​‍​​‍​‍​​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​‍‍‍​​‍‍​​​​‍​‍‍‍​​​​​‍‍‍​​​​​‍‍​​‍​‍​‍‍​‍‍‍​​‍‍​​‍​​​​‍​‍​​​​‍‍​​​‍‍​‍‍​‍​​​​‍‍​​​​‍​‍‍‍​​‍​​​‍​‍​​‍​​​​‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​‍​​‍​‍‍​​‍‍​​​‍​​​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍‍‍​‍​‍​‍‍‍​​‍​​‍‍​‍‍‍​​​‍​​​​​​‍‍​​​‍​​‍‍​‍​​‍​‍‍​‍‍‍​​​‍‍​​‍​​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍​​‍​‍‍‍‍‍​‍‍‍​‍‍​​‍‍​‍​​‍​‍‍​​​​‍​‍‍​​​‍​​​‍‍​​​‍​​‍‍​‍‍​​​‍​‍​​​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​​‍‍​‍‍​‍‍‍‍​‍‍​​‍​​​‍‍​​‍​‍​​‍​‍​​​​​‍​​‍‍‍​​‍​​‍‍‍​​‍​‍‍‍​​‍‍​‍​‍​​‍‍​‍‍‍‍​‍‍​‍​​‍​‍‍​‍‍‍​​​‍​‍​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​‍​​‍​​‍​‍​​‍​​‍​‍​​‍​​​​‍​‍​​​​​‍​‍​​​​​‍​‍​​‍​​​​​​​‍‍​​​‍‍​‍‍​‍‍​​​‍‍​‍​​‍​‍‍​​​‍‍​‍‍​‍​‍‍​​‍​‍‍‍​​‍‍​​​‍‍​‍‍​‍‍‍‍​‍‍​‍‍​‍​‍‍​‍‍​‍​‍‍​​​​‍​‍‍​‍‍‍​​‍‍​​‍​​​​‍​‍​​​​​‍​‍​​‍​​​​‍​‍​​‍​​​​​​​‍‍​​​‍‍​‍‍​‍‍​​​‍‍​‍​​‍​‍‍​​​‍‍​‍‍​‍​‍‍​​‍​‍‍‍​​‍‍​‍‍‍‍​‍‍‍​​​​​‍‍‍​‍​​​‍‍​‍​​‍​‍‍​‍‍‍‍​‍‍​‍‍‍​​​‍​‍​​​​​‍​​‍‍‍​​‍​‍‍​‍​​‍​‍‍​‍​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​​‍​​‍‍‍​​‍​‍‍​​​​‍​​​​​​​‍​​‍‍‍​​‍​‍‍​‍​‍‍‍​​‍‍​​‍​​‍‍‍​​‍​‍‍​​​​‍​​​​​​‍‍‍​‍​​​‍‍‍‍​​‍​‍‍‍​​​​​‍‍​​‍​‍​​‍‍‍‍​‍​‍‍​​​‍‍​‍‍​‍‍​​​‍‍​‍​​‍​‍‍​​​‍‍​‍‍​‍​‍‍​​‍​‍‍‍​​‍​​​‍‍​​‍‍​‍​​‍​‍‍​‍‍​​​‍‍​​‍​‍​​‍​‍​​​​​‍​​‍‍‍​‍‍‍​​‍​​‍‍​​​‍​​​‍​​‍‍‍​​‍​‍​​‍​​‍​‍‍​​​​‍​​​​​​‍‍​‍​​​​‍‍​​‍​‍​‍‍​‍‍​​​‍‍‍​​​​​​‍‍‍‍​‍​​‍​​‍‍‍​‍​​​‍‍​​‍‍​‍​​‍​‍‍​‍‍​​​‍‍​​‍​‍​‍‍​‍‍‍​​‍‍​​​​‍​‍‍​‍‍​‍​‍‍​​‍​‍​​‍​​​​​​‍‍​‍‍‍‍​‍‍​​‍‍​​​‍​​​​​​‍‍‍​‍​​​‍‍​‍​​​​‍‍​​‍​‍​​‍​​​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​​‍​​​​​​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​​‍‍‍​​‍​‍​​‍​​​​‍​‍​​‍​​​​​​​‍‍​​​‍‍​‍‍​‍‍​​​‍‍​‍​​‍​‍‍​​​‍‍​‍‍​‍​‍‍​​‍​‍‍‍​​‍‍​​​​‍​‍‍‍​​‍​​‍‍​​‍‍‍​‍‍‍​‍​‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍​‍‍‍​​‍‍‍​‍​​​​‍​‍​​​​​‍​​‍‍‍​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​​‍‍​‍‍​‍​​‍​‍‍​​‍‍‍​‍‍​‍​​​​‍‍‍​‍​​​​‍​​‍‍‍​​‍​‍‍​​​​‍​​​​​​‍‍‍​‍​​​‍‍‍‍​​‍​‍‍‍​​​​​‍‍​​‍​‍​​‍‍‍‍​‍​‍‍​​​‍‍​‍‍​‍‍​​​‍‍​‍​​‍​‍‍​​​‍‍​‍‍​‍​‍‍​​‍​‍‍‍​​‍​​​‍‍​​‍‍​‍​​‍​‍‍​‍‍​​​‍‍​​‍​‍​​‍​‍​​​​​‍​​‍‍‍​‍‍‍​​‍​​‍‍​​​‍​​​‍​‍​‍‍​​‍​​‍‍‍​​‍​‍​​‍​​‍​‍​​‍​​​​‍​‍​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​‍‍​​​‍​​​​​​‍‍​​​‍‍​‍‍​‍‍​​​‍‍​‍​​‍​​‍​‍​​​​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​​‍‍​‍‍​‍​​‍​‍‍​​‍‍‍​‍‍​‍​​​​‍‍‍​‍​​​​‍​‍‍​​​​‍​​​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​​‍​‍​​‍​​‍‍‍​‍​​​​​‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​‍​​‍​‍‍​​‍‍​​​‍​​​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​‍‍​​‍​​​​​​‍​​‍​​‍​‍‍​​‍‍​​​‍​​​​​​‍‍​​​​‍​​‍​​​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​​‍​​​​​​‍‍​​‍​‍​‍‍‍‍​​​​‍‍​‍​​‍​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍‍​​‍​‍‍​​​​‍​​​​​​‍‍​​​​‍​‍‍‍​​​​​‍‍‍​​​​​‍‍​​‍​‍​‍‍​‍‍‍​​‍‍​​‍​​​​‍​​​​​​‍‍​‍​​‍​‍‍‍​‍​​​​‍​​​​​​‍‍‍​‍​​​‍‍​‍‍‍‍​​‍​​​​​​‍‍‍​‍​​​‍‍​‍​​​​‍‍​​‍​‍​​‍​​​​​​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​​‍‍​‍‍​‍​​‍​‍‍​​‍‍‍​‍‍​‍​​​​‍‍‍​‍​​​​‍​​​​​​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​​​​​​​‍‍‍‍​‍​​‍​​​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​​‍​‍‍‍​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍​​​​‍​‍‍​​‍​​​​‍​‍​​​​​‍​‍​​‍​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​​‍‍​‍‍​‍​​‍​‍‍​​‍‍‍​‍‍​‍​​​​‍‍‍​‍​​​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​​​​​​​‍‍‍‍​‍​​‍​​​​​​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​​‍‍​‍‍​‍​​‍​‍‍​​‍‍‍​‍‍​‍​​​​‍‍‍​‍​​​​‍​‍‍‍​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍​​​​‍​‍‍​​‍​​​​‍​‍​​​​​‍​‍​​‍​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​​‍‍​‍‍​‍​​‍​‍‍​​‍‍‍​‍‍​‍​​​​‍‍‍​‍​​​​‍​‍‍‍​​‍‍‍​‍‍‍​‍‍‍​​‍​​‍‍​‍​​‍​‍‍‍​‍​​​‍‍​​‍​‍​​‍​‍​​​​‍‍​‍​​​​‍‍​‍​​‍​‍‍​​‍​​​‍‍​​‍​‍​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​‍​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​‍​​‍​​‍​‍‍‍​​‍‍​​‍​‍​‍‍​‍‍‍​​‍‍​​​‍‍​‍‍​‍‍‍‍​‍‍​​‍​​​‍‍​​‍​‍​​‍​‍​​​​​‍​​‍‍‍​‍‍‍​‍​‍​‍‍‍​‍​​​‍‍​​‍‍​​​‍​‍‍​‍​​‍‍‍​​​​​‍​​‍‍‍​​‍​‍​​‍​​‍​‍​​‍​​​​‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​​​‍‍​‍‍​‍‍​​​‍‍​‍​​‍​‍‍​​​‍‍​‍‍​‍​‍‍​​‍​‍‍‍​​‍‍​​‍​‍​‍‍​​​‍‍​‍‍​‍​​​​‍‍​‍‍‍‍​​‍​‍​​​​​‍​​‍‍‍​‍​‍‍​‍‍​‍​​‍‍‍‍​‍​​‍​‍‍​‍​‍‍‍​‍​​‍​​​​​​‍​​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​​​​​​‍‍​​​​‍​‍‍​​‍​​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​​‍​​​​‍​​​​​​‍‍‍​‍​​​‍‍​‍‍‍‍​​‍​​​​​​‍‍‍‍​‍‍​​‍‍​​​​​‍‍‍‍‍​‍​​‍​​‍‍‍​​‍​‍‍‍​​‍‍​​‍‍​​‍‍​‍‍‍‍​‍‍‍​​‍​​‍‍​‍‍​‍​‍‍​​​​‍​‍‍‍​‍​​​​‍​‍​​​​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​​‍‍​‍‍​‍​​‍​‍‍​​‍‍‍​‍‍​‍​​​​‍‍‍​‍​​​​‍​‍​​‍​​‍​‍​​‍​​​​‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​​‍​‍​‍‍​‍‍​​​‍‍‍​​‍‍​‍‍​​‍​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​‍‍​​‍​​​​​​‍​​‍​​‍​‍‍​​‍‍​​​‍​​​​​​‍‍​‍‍‍​​‍‍​‍‍‍‍​​‍​​​​​​‍‍‍​​‍‍​‍‍​​‍​‍​‍‍​​​‍‍​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​​‍​​​​​​‍‍​​‍​‍​‍‍‍‍​​​​‍‍​‍​​‍​‍‍‍​​‍‍​‍‍‍​‍​​​‍‍‍​​‍‍​​‍​‍‍​​​​‍​​​​​​‍‍‍​‍​​​‍‍‍​​‍​​‍‍‍‍​​‍​​‍​​​​​​‍‍‍​‍​​​‍‍​‍‍‍‍​​‍​​​​​​‍‍​​‍​‍​‍‍‍‍​​​​‍‍‍​‍​​​‍‍‍​​‍​​‍‍​​​​‍​‍‍​​​‍‍​‍‍‍​‍​​​​‍​​​​​​‍‍​​​​‍​​‍​​​​​​‍‍​‍​​​​‍‍​‍​​‍​‍‍​​‍​​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​‍‍‍​​​‍​​​​​​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​​​​​​‍‍​​‍‍​​‍‍‍​​‍​​‍‍​‍‍‍‍​‍‍​‍‍​‍​​‍​​​​​​‍‍‍​‍​​​‍‍​‍​​​​‍‍​​‍​‍​​‍​​​​​​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​​‍‍​‍‍​‍​​‍​‍‍​​‍‍‍​‍‍​‍​​​​‍‍‍​‍​​​​‍​​​​​​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​​​​​​​‍‍‍‍​‍​​‍​​​​​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍‍​‍​​​‍‍‍​​‍​​‍‍​‍​​‍​‍‍​​‍​‍​‍‍‍​‍‍​​‍‍​​‍​‍​‍​‍‍‍‍‍​‍‍​‍​​​​‍‍​‍​​‍​‍‍​​‍​​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​‍‍‍​​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​‍​​​​‍‍‍​​​​​‍‍​‍‍​​​‍‍​​​​‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍‍‍​​‍‍​‍‍​‍​​‍​‍‍​​‍‍‍​‍‍​‍​​​​‍‍‍​‍​​​​‍​‍‍‍​​‍‍‍​​‍​​‍‍​​‍​‍​‍‍​​​​‍​‍‍​​‍​​​​‍​‍​​​​​‍​‍​​‍​​‍​‍​​‍​​​​‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​‍​​‍​‍‍​​‍‍​​​‍​​​​​​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​​​‍‍​‍‍​‍‍​​​‍‍​‍​​‍​‍‍​​​‍‍​‍‍​‍​‍‍​​‍​‍‍‍​​‍‍​​‍​‍​‍‍​​​‍‍​‍‍​‍​​​​‍‍​‍‍‍‍​​‍​‍​​​​​‍​​‍‍‍​‍​‍‍​‍‍​‍​​‍‍‍‍​‍​​‍​‍‍​‍​‍‍‍​‍​​‍​​​​​​‍​​‍​​​​‍‍​‍​​‍​‍‍​​‍​​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​‍‍‍​​​‍​​​​​​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​​​​​​‍‍​​‍‍​​‍‍​‍‍‍‍​‍‍‍​‍​‍​‍‍​‍‍‍​​‍‍​​‍​​​​‍‍‍​‍​​​‍​​​​​​‍‍‍‍​‍‍​​‍‍​​​​​‍‍‍‍‍​‍​​‍​​‍‍‍​​‍​‍‍‍​​‍‍​​‍‍​​‍‍​‍‍‍‍​‍‍‍​​‍​​‍‍​‍‍​‍​‍‍​​​​‍​‍‍‍​‍​​​​‍​‍​​​​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​‍​​‍​​‍​‍​​‍​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​​‍​‍​‍‍​‍‍​​​‍‍‍​​‍‍​‍‍​​‍​‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​​​‍‍​‍‍​‍‍​​​‍‍​‍​​‍​‍‍​​​‍‍​‍‍​‍​‍‍​​‍​‍‍‍​​‍‍​​‍​‍​‍‍​​​‍‍​‍‍​‍​​​​‍‍​‍‍‍‍​​‍​‍​​​​​‍​​‍‍‍​‍​‍‍​‍‍​‍​​‍‍‍‍​‍​​‍​‍‍​‍​‍‍‍​‍​​‍​​​​​​‍​​‍‍‍​​‍‍​‍‍‍‍​​‍​​​​​​‍‍​‍​​​​‍‍​‍​​‍​‍‍​​‍​​​‍‍​​‍​​​‍‍​​‍​‍​‍‍​‍‍‍​​​‍​​​​​​‍‍​‍‍​‍​‍‍​​‍​‍​‍‍‍​​‍‍​‍‍‍​​‍‍​‍‍​​​​‍​‍‍​​‍‍‍​‍‍​​‍​‍​​‍​​​​​​‍‍​​‍‍​​‍‍​‍‍‍‍​‍‍‍​‍​‍​‍‍​‍‍‍​​‍‍​​‍​​​​‍​​​​​​‍‍​‍​​‍​‍‍​‍‍‍​​​‍​​​​​​‍‍‍​‍​​​‍‍​‍​​​​‍‍​‍​​‍​‍‍‍​​‍‍​​‍​​​​​​‍‍​​‍‍​​‍‍​‍​​‍​‍‍​‍‍​​​‍‍​​‍​‍​​‍​‍‍‍​​​‍​​‍‍‍​​‍​‍​​‍​​​​‍​‍​​​​​‍​‍​​​​​‍​‍​​‍‍​‍​​‍​‍‍​​‍‍​​​‍​​​​​​‍​‍‍‍‍‍​‍​‍‍‍‍‍​‍‍​‍‍‍​​‍‍​​​​‍​‍‍​‍‍​‍​‍‍​​‍​‍​‍​‍‍‍‍‍​‍​‍‍‍‍‍​​‍​​​​​​​‍‍‍‍​‍​​‍‍‍‍​‍​​‍​​​​​​​‍​​‍‍‍​‍​‍‍‍‍‍​‍​‍‍‍‍‍​‍‍​‍‍​‍​‍‍​​​​‍​‍‍​‍​​‍​‍‍​‍‍‍​​‍​‍‍‍‍‍​‍​‍‍‍‍‍​​‍​​‍‍‍​​‍‍‍​‍​​​​​‍​‍​​​‍​​​​​​​‍​​​​​​​‍​​​​​​​‍​​​​​​‍‍​​​‍‍​‍‍​‍‍​​​‍‍​‍​​‍​​‍​‍​​​​​‍​‍​​‍​​​​‍​‍​​​‍​​​‍‍
