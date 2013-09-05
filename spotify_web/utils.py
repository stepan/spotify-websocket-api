import binascii


base62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


class SpotifyUtil():
    @staticmethod
    def gid2id(gid):
        return binascii.hexlify(gid).rjust(32, "0")

    @staticmethod
    def id2uri(uritype, v):
        res = []
        v = int(v, 16)
        while v > 0:
            res = [v % 62] + res
            v /= 62
        guid = ''.join([base62[i] for i in res])
        return ("spotify:" + uritype + ":" + guid).rjust(22, "0")

    @staticmethod
    def uri2id(uri):
        parts = uri.split(":")
        if len(parts) > 3 and parts[3] == "playlist":
            s = parts[4]
        else:
            s = parts[2]

        v = 0
        for c in s:
            v = v * 62 + base62.index(c)
        return hex(v)[2:-1].rjust(32, "0")

    @staticmethod
    def gid2uri(uritype, gid):
        guid = SpotifyUtil.gid2id(gid)
        uri = SpotifyUtil.id2uri(uritype, guid)
        return uri

    @staticmethod
    def get_uri_type(uri):
        uri_parts = uri.split(":")

        if len(uri_parts) >= 3 and uri_parts[1] == "local":
            return "local"
        elif len(uri_parts) >= 5:
            return uri_parts[3]
        elif len(uri_parts) >= 4 and uri_parts[3] == "starred":
            return "playlist"
        elif len(uri_parts) >= 3:
            return uri_parts[1]
        else:
            return False

    @staticmethod
    def is_local(uri):
        return SpotifyUtil.get_uri_type(uri) == "local"


def gid2id(gid):
    return binascii.hexlify(gid).rjust(32, "0")


def id2uri(uritype, v):
    res = []
    v = int(v, 16)
    while v > 0:
        res = [v % 62] + res
        v /= 62
    guid = ''.join([base62[i] for i in res])
    return ("spotify:" + uritype + ":" + guid).rjust(22, "0")


def uri2id(uri):
    parts = uri.split(":")
    if len(parts) > 3 and parts[3] == "playlist":
        s = parts[4]
    else:
        s = parts[2]

    v = 0
    for c in s:
        v = v * 62 + base62.index(c)
    return hex(v)[2:-1].rjust(32, "0")


def gid2uri(uritype, gid):
    guid = SpotifyUtil.gid2id(gid)
    uri = SpotifyUtil.id2uri(uritype, guid)
    return uri


def get_uri_type(uri):
    uri_parts = uri.split(":")

    if len(uri_parts) >= 3 and uri_parts[1] == "local":
        return "local"
    elif len(uri_parts) >= 5:
        return uri_parts[3]
    elif len(uri_parts) >= 4 and uri_parts[3] == "starred":
        return "playlist"
    elif len(uri_parts) >= 3:
        return uri_parts[1]
    else:
        return False


def is_local(uri):
    return SpotifyUtil.get_uri_type(uri) == "local"