package hello.hellospring.controller;

import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

@Controller
public class MemberController {

    private final MemberService memberService;
//    @Autowired private MemberService memberService;
    /*
    * 필드 주입 비추
    * 변경 힘듬
    *
    * setter로 DI 주입하는 방법도 있음
    * setter로 주입하면 public으로 노출됨 -> 조심해야함 -> 권장x
    *
    * 상황에 따라 구현 클래스 변경하려면 설정을 통해 등록하는게 좋음 -> 코드 수정 필요하지 않으므로
    * */

    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }
}
