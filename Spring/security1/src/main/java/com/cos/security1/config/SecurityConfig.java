package com.cos.security1.config;

import com.cos.security1.config.oauth.PrincipalOauth2UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableWebSecurity // spring security filter가 spring filter chain에 등록됨
@EnableGlobalMethodSecurity(securedEnabled = true, prePostEnabled = true) // secured 어노테이션 활성화, preAuthorized, poserAuthorized 어노테이션 활성화
public class SecurityConfig {

    @Autowired
    private PrincipalOauth2UserService principalOauth2UserService;

    // 해당 메서드의 리턴되는 오프젝트는 IoC로 등록해줌
    @Bean
    public BCryptPasswordEncoder encodePwd() {
        return new BCryptPasswordEncoder();
    }

    // filterChain 메서드에서 정의한 규칙에 따라 엔드포인트를 보호
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {

        http.csrf().disable();
        http.authorizeRequests()
                .antMatchers("/user/**").authenticated()
                .antMatchers("/manager/**").access("hasRole('ROLE_ADMIN') or hasRole('ROLE_MANAGER')")
                .antMatchers("/admin/**").access("hasRole('ROLE_ADMIN')")
                .anyRequest().permitAll()
                .and()
                .formLogin()
                .loginPage("/login") // 인증 필요하면 보내버리는 곳 지정
                .loginProcessingUrl("/login") // login 주소가 호출이 되면 시큐리티가 낚아채서 대신 로그인 진행 -> Controller에 "/login" 안만들어도됨
                .defaultSuccessUrl("/") // 로그인 성공하면 어디로 보내는지 정할 수 있음
                .and()
                .oauth2Login()
                .loginPage("/login")
                // Oauth2후처리 필요. 1.코드받기(인증) 2.엑세스 토큰(권한)
                // 3.사용자프로필 정보 가져와서 4.그 정보를 토대로 회원가입 자동으로 진행시키기도 함
                // 4-2 회원가입 시 추가정보 필요할 수 있음
                .userInfoEndpoint()
                .userService(principalOauth2UserService);
        return http.build();
    }
}
