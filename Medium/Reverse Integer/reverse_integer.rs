impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut new_string:String=String::new();
        let mut x_string = x.to_string();
        if x<0{
            new_string.push('-');
            while x_string!="-"{
                new_string.push(x_string.pop().unwrap());
            }
            if new_string.parse::<i64>().unwrap() < -2147483648 {return 0;}
            else { return new_string.parse::<i32>().unwrap();}
        }
        else{
            while x_string!=""{
                new_string.push(x_string.pop().unwrap());
            }
            if new_string.parse::<i64>().unwrap() > 2147483647 {return 0;}
            else { return new_string.parse::<i32>().unwrap();}
        }
        
    }
}