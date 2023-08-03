package com.cos.security1.repository;

import com.cos.security1.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

// CRUD 함수를 JpaRepository가 들고 있음.
// @Repository라는 어노테이션이 없어도 IoC됨, 이유는 JpaRepository를 상속했기 때문에
public interface UserRepository extends JpaRepository<User, Integer> {
    // findBy규칙 -> Username문법 == select *from user where username= {username}
    public User findByUsername(String username); // Jpa name 함수

    public User findByEmail(String email);
}
