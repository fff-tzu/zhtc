package com.chao.mapper;
import org.apache.ibatis.annotations.Update;
import com.chao.pojo.User;
import org.apache.ibatis.annotations.Delete;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface userMapper {

    @Select("select * from users where username = #{username} and password = #{password}")
    User getByusernameAndPassword(User user);

    @Insert("insert into users (username, password) " +
            "VALUES(#{username},#{password})")
    void insert(User user);
    // 找到 userMapper.java，在里面添加这几行
    @Update("update users set password = #{password} where username = #{username}")
    void updatePassword(User user);
}
