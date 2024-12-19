fun main() {

    val n = readln().toInt()
    var a= 0
    var b=1
    var tmp =0

    for(i in 0..n-1){
        a = b
        b = tmp
        tmp = a+b
    }
    println(tmp)
}
