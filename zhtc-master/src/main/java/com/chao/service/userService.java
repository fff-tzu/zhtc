package com.chao.service;

import com.chao.pojo.User;

public interface userService {
    User login(User user);

    void add(User user);
    // 找到 userService.java 接口，添加这一行
    void updatePassword(User user);
}
