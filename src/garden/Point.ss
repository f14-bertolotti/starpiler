class Point {
    var double x;
    var double y;
    
    fun (Point,double,double->Point) __init__(this, x, y) {
        this.x = x;
        this.y = y;
        return this;
    }
    fun (Point,Point->Point) add(this, other) {
        this.x = this.x + other.x;
        this.y = this.y + other.y;
        return this;
    }
}
