import time


def wait(method, timeout=10, err=Exception, check=False, interval=1, **kwargs ):
    st_time = time.time()

    while time.time() < st_time + timeout:
        try:
            result = method(**kwargs)
            if check:
                if result:
                    return result
            else:
                return result
        except err as e:
            print(f'{e=}')
        time.sleep(interval)

    raise TimeoutError(f"Timeout was reached during operation '{method.__name__}'. See details in debug log.")