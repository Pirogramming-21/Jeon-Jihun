// 게임 초기화(시도가능 횟수 설정, 3자리 숫자 설정, input창 비우기)
// 시도 가능 횟수 설정
let try_cnt = 9;

// input창 비우는 함수 제작
const input_nums = document.querySelectorAll("input[type=text");

function reset(){
    input_nums[0].value="";
    input_nums[1].value="";
    input_nums[2].value="";
}

// 3자리 숫자 설정
const numbers = [];
for (let n=1; n <= 9; n++) {
    numbers.push(n);
}

const answer = [];
for (let n=0; n < 3; n++) {
    const index = Math.floor(Math.random() * numbers.length);
    answer.push(numbers[index]);
    numbers.splice(index, 1);
} 


// 게임 시작
function check_numbers() {
    let num1 = input_nums[0].value;
    let num2 = input_nums[1].value;
    let num3 = input_nums[2].value;

    // 빈칸 있으면 초기화
    if (num1 === "" || num2 === "" || num3 === "") {
        reset();
        return;
    }

    // 스트라이크, 볼 카운트
    let strike = 0;
    let ball = 0;
    try_cnt--;

    for (let i=0; i<3; i++) {
        for (let j=0; j<3; j++) {
            if (input_nums[i].value==answer[j]){
                if (i==j) {
                    strike++;
                } else {
                    ball++;
                }
                break
            }
        }
    }

    // HTML에 표시하기(아래 형식에 준함)
    // <div class="check-result">
    //     <div class="left">6 0 2</div>
    //     :
    //     <div class="right">
    //         0 <div class="strike num-result">S</div>
    //         1 <div class="ball num-result">B</div>
    //     </div>
    // </div>

    const CHK_result = document.createElement('div');
    CHK_result.className = "check-result";

    const content_left = document.createElement('div');
    content_left.className = "left";
    content_left.innerText = num1+ " "+ num2+ " "+ num3 ;
    CHK_result.appendChild(content_left);

    CHK_result.append(":");

    const content_right = document.createElement('div');
    content_right.className = "right";
    CHK_result.appendChild(content_right);

    const div_strike = document.createElement('div');
    const div_ball = document.createElement('div');
    const div_out = document.createElement('div');
    div_strike.className = "strike num-result";
    div_ball.className = "ball num-result";
    div_out.className = "out num-result";

    if (strike == 0 && ball == 0) {
        content_right.appendChild(div_out);
        div_out.innerText = "O";
    } else {
        content_right.append(strike);
        div_strike.innerText = "S";
        content_right.appendChild(div_strike);
        content_right.append(ball);
        div_ball.innerText = "B";
        content_right.appendChild(div_ball);
    }
    
    document.querySelector('.result-display').appendChild(CHK_result);

    // 확인하기 버튼 비활성화 함수
    function disable_btn() {
        const submitBtn = document.querySelector('.submit-button');
        submitBtn.disabled = true;
    }

    // 결과 창 출력
    const result_img = document.getElementById('game-result-img');
    if (strike == 3) {
        result_img.src = './success.png';
        disable_btn();
        return;
    } else if (try_cnt == 0) {
        result_img.src = './fail.png';
        disable_btn();
        return;
    }

    // 다음 숫자 입력을 위한 초기화
    reset();
} 
