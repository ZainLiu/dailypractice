class RedisLock(TmpModel):
    @classmethod
    def lock(cls, name, timeout=60):
        now_stamp = time.time()
        try_lock = cls.setnx(name, now_stamp + timeout + 1)
        if try_lock:  # 锁成功
            cls.expire(name, timeout)
            return True
        # 其他人已锁，则先判断是否已过期，过期则尝试获取锁
        old_stamp = cls.get(name)
        if old_stamp and float(old_stamp) >= now_stamp:  # 锁还没有过期
            return False
        # 如果设时间的时候发现被别人抢先设了，则抢锁失败
        replace_stamp = cls.getset(name, now_stamp + timeout + 1)
        if old_stamp == replace_stamp:
            return True
        else:
            return False

    @classmethod
    def unlock(cls, name):
        cls.delete(name)