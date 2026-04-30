package com.chao.service;

import com.chao.mapper.userMapper;
import com.chao.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.time.LocalDateTime;

@Service
public class userServiceImpl implements userService{
    @Autowired
    private userMapper userMapper;

    @Override
    public User login(User user) {
        return userMapper.getByusernameAndPassword(user);
    }

    @Override
    public void add(User user) {
        userMapper.insert(user);
    }
    // 找到 userServiceImpl.java，添加这个实现方法
    @Override
    public void updatePassword(User user) {
        userMapper.updatePassword(user);
    }
}
