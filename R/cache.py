if False:
    # 仅用于类型检查
    from .Result import Result
    from .R import R

# {..., k: (share_l, share_iter)}
cache = {}


def cache_clear():
    cache.clear()


def cache_deco(imatch):
    '''
    缓存 R 中 imatch 的修饰器
    '''

    def memo_imatch(self: 'R', resource: str, prev_result: 'Result'):
        k = (id(self), id(resource), str(prev_result))
        share_l, share_iter = cache.setdefault(k, ([], imatch(self, resource, prev_result)))
        yield from share_l

        while True:
            try:
                echo = next(share_iter)
            except StopIteration:
                break
            share_l.append(echo)
            yield echo

    return memo_imatch