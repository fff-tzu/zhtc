package com.chao.controller;

import com.chao.pojo.Result;
import com.chao.pojo.User;
import com.chao.service.userService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@Slf4j
@RestController
@CrossOrigin(origins = "*") // 【关键】允许所有来源跨域，防止前端请求被拦截
@RequestMapping("/user")    // 建议加上统一前缀
public class userController {

    @Autowired
    private userService userService;

    /**
     * 用户登录
     */
    @PostMapping("/login")
    public Result login(@RequestBody User user){
        log.info("用户登录：{}", user);
        User e = userService.login(user);
        
        if(e != null) {
            // 建议返回用户信息，前端可以根据权限跳转 user 或 admin
            return Result.success(e); 
        } else {
            return Result.error("用户名或密码错误");
        }
    }

    /**
     * 用户注册
     */
    @PostMapping("/register") // 将 /reg 改为 /register 对应前端 fetch 地址
    public Result register(@RequestBody User user){
        log.info("用户注册请求：{}", user);
        
        // 1. 先根据用户名查询是否已存在（这里假设你的 service 有这个方法）
        // 如果没有 getByUsername，可以用 login(user) 逻辑判断，但最好是专表专查
        User existUser = userService.login(user); 

        if(existUser != null){
            return Result.error("用户名已存在，请直接登录");
        } else {
            userService.add(user); // 调用你的写入数据库方法
            return Result.success();
        }
    }

    @PostMapping("/update")
    public Result update(@RequestBody User user) {
        log.info("重置密码请求：{}", user.getUsername());
        // 这里调用你的 service 执行更新 SQL:
        // update users set password = #{password} where username = #{username}
        userService.updatePassword(user);
        return Result.success();
    }
}