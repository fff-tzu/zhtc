package com.chao;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;

@ServletComponentScan
@SpringBootApplication
public class WebCoursedesignApplication {

    public static void main(String[] args) {
        SpringApplication.run(WebCoursedesignApplication.class, args);
    }

}
