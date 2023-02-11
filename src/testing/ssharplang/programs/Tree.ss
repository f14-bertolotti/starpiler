from "src/testing/ssharplang/programs/String.ss" import String as String;


class Node {
    var Node left;
    var Node right;
    var String name;
    var int64 hasLeft;
    var int64 hasRight;

    fun (Node, String -> Node) __init__(this, name) {
        this.name = name;
        this.hasLeft = 0;
        this.hasRight = 0;
        return this;
    }

    fun (Node, Node -> Node) setLeft(this, node) {
        this.hasLeft = 1;
        this.left = node;
        return this;
    }

    fun (Node, Node -> Node) setRight(this, node) {
        this.hasRight = 1;
        this.right = node;
        return this;
    }

    fun (Node -> String) toString(this) {
        String result = this.name.clone();
        result.concat(new String("("));
        if (this.hasLeft == 1) {result.concat(this.left.toString());}
        if (this.hasLeft == 0) {result.concat(new String("--"));}
        result.concat(new String(",")); 
        if (this.hasRight == 1) {result.concat(this.right.toString());}
        if (this.hasRight == 0) {result.concat(new String("--"));}
        result.concat(new String(")"));
        return result;
    }

    fun (->int64) __main__() {

        Node root = new Node(new String("root"));
        root.setLeft(new Node(new String("root.left")));
        root.setRight(new Node(new String("root.right")));
        root.left.setLeft(new Node(new String("root.left.left")));
        root.right.setRight(new Node(new String("root.left.right")));
        
        gccollect();

        return root.toString().equals(new String("root(root.left(root.left.left(--,--),--),root.right(--,root.left.right(--,--)))"));
    }

}





