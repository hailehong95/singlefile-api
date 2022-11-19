#!/usr/bin/env python

import re
import os
import click
import requests
import unicodedata

from lxml.html import fromstring


BASE_URL = "http://127.0.0.1:8080"


def sanitize_name(value, allow_unicode=False):
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def singlefile(target):
    try:
        data = {"url": target}
        rq = requests.post(url=BASE_URL, data=data)
        tree = fromstring(rq.content)
        filename = sanitize_name(tree.findtext(".//title"))
        filename += ".html"
    except Exception as ex:
        print(ex)
    else:
        return filename, rq.content


def save_response(filename, path, content):
    try:
        full_path = os.path.join(path, filename)
        with open(full_path, "wb") as fs:
            fs.write(content)
    except Exception as ex:
        print(ex)


@click.group()
def cli():
    """A CLI for SingleFile Client"""
    pass


@cli.command(name="save", help="Save a URL into a single HTML file")
@click.option("-u", "--url", type=str, help="--url=http://example.com", required=True)
@click.option("-p", "--path", default=".", type=str, help="--path=.|path=/path/to/report/")
def save_single(url, path):
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.exists(path):
        return
    filename, content = singlefile(url)
    save_response(filename, path, content)


@cli.command(name="bulk", help="Save list URL to each single HTML file")
@click.option("-us", "--urls", type=str, help="--list=urls.txt", required=True)
@click.option("-p", "--path", type=str, help="--path=.|path=/path/to/report/", required=True)
def save_bulk(urls, path):
    if not os.path.exists(urls):
        return
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.exists(path):
        return
    try:
        lines = []
        with open(urls) as fs:
            lines = fs.read().splitlines()
        for url in lines:
            filename, content = singlefile(url)
            save_response(filename, path, content)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    cli()
