; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

%"struct.LinkedNode" = type {%"struct.LinkedNode"*, i8*, i64, i64, %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)*, i64 (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*)*, i64 (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)*, void (%"struct.LinkedNode"*)*}
%"struct.GC" = type {%"struct.LinkedNode"*, %"struct.LinkedNode"*, %"struct.GC"* (%"struct.GC"*)*, i8* (%"struct.GC"*, i8*, i64)*, i8* (%"struct.GC"*, i8*, i64)*, %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*, i8*)*, %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)*, void (%"struct.GC"*)*}
%"struct.Integer" = type {i64, %"struct.Integer"* (%"struct.Integer"*, i64)*, void (%"struct.Integer"*)*}
%"struct.IntArray" = type {%"struct.Integer"*, i64, %"struct.IntArray"* (%"struct.IntArray"*, i64)*, void (%"struct.IntArray"*)*}
declare i8* @"memcpy"(i8* %".1", i8* %".2", i64 %".3")

@"__memcpy140385256897888" = internal global i8* (i8*, i8*, i64)* undef
declare i8* @"malloc"(i64 %".1")

@"__malloc140385251988752" = internal global i8* (i64)* undef
declare void @"free"(i8* %".1")

@"__free140385259166384" = internal global void (i8*)* undef
@"__memcpy140385250703392" = internal global i8* (i8*, i8*, i64)* undef
@"__malloc140385250699696" = internal global i8* (i64)* undef
@"__free140385250702192" = internal global void (i8*)* undef
@"__free140385254917408" = internal global void (i8*)* undef
declare i64 @"printf"(i8* %".1", ...)

define %"struct.LinkedNode"* @"start5751983272486680366140385253942144"(%"struct.LinkedNode"* %".1", i8* %".2", i64 %".3")
{
.5:
  %".6" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".1", %"struct.LinkedNode"** %".6"
  %".8" = alloca i8*
  store i8* %".2", i8** %".8"
  %".10" = alloca i64
  store i64 %".3", i64* %".10"
  %".12" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".13" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".6"
  %".14" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".13", i64 0, i32 0
  store %"struct.LinkedNode"* %".12", %"struct.LinkedNode"** %".14"
  %".16" = load i8*, i8** %".8"
  %".17" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".6"
  %".18" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".17", i64 0, i32 1
  store i8* %".16", i8** %".18"
  %".20" = load i64, i64* %".10"
  %".21" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".6"
  %".22" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".21", i64 0, i32 2
  store i64 %".20", i64* %".22"
  %".24" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".6"
  %".25" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".24", i64 0, i32 3
  store i64 0, i64* %".25"
  %".27" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".6"
  ret %"struct.LinkedNode"* %".27"
}

define i64 @"isLast5536074550656775930140385253936288"(%"struct.LinkedNode"* %".1")
{
.3:
  %".4" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".1", %"struct.LinkedNode"** %".4"
  %".6" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".7" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".6", i64 0, i32 0
  %".8" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".7"
  %".9" = ptrtoint %"struct.LinkedNode"* %".8" to i64
  %".10" = icmp eq i64 %".9", 0
  %".11" = select  i1 %".10", i64 1, i64 0
  %".12" = icmp eq i64 %".11", 1
  br i1 %".12", label %".3.if", label %".3.endif"
.3.if:
  ret i64 1
.3.endif:
  ret i64 0
}

define %"struct.LinkedNode"* @"getLast3120310538166611506140385253944880"(%"struct.LinkedNode"* %".1")
{
.3:
  %".4" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".1", %"struct.LinkedNode"** %".4"
  %".6" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".7" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".6", %"struct.LinkedNode"** %".7"
  %".9" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".6", i64 0, i32 5
  %".10" = load i64 (%"struct.LinkedNode"*)*, i64 (%"struct.LinkedNode"*)** %".9"
  %".11" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".7"
  %".12" = call i64 %".10"(%"struct.LinkedNode"* %".11")
  %".13" = icmp eq i64 %".12", 1
  br i1 %".13", label %".3.if", label %".3.endif"
.3.if:
  %".15" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  ret %"struct.LinkedNode"* %".15"
.3.endif:
  %".17" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".18" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".17", i64 0, i32 0
  %".19" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".18"
  %".20" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".19", %"struct.LinkedNode"** %".20"
  %".22" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".19", i64 0, i32 6
  %".23" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".22"
  %".24" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".20"
  %".25" = call %"struct.LinkedNode"* %".23"(%"struct.LinkedNode"* %".24")
  ret %"struct.LinkedNode"* %".25"
}

define i64 @"size3858513429958943938140385251897072"(%"struct.LinkedNode"* %".1")
{
.3:
  %".4" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".1", %"struct.LinkedNode"** %".4"
  %".6" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".7" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".6", %"struct.LinkedNode"** %".7"
  %".9" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".6", i64 0, i32 5
  %".10" = load i64 (%"struct.LinkedNode"*)*, i64 (%"struct.LinkedNode"*)** %".9"
  %".11" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".7"
  %".12" = call i64 %".10"(%"struct.LinkedNode"* %".11")
  %".13" = icmp eq i64 %".12", 1
  br i1 %".13", label %".3.if", label %".3.endif"
.3.if:
  ret i64 1
.3.endif:
  %".16" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".17" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".16", i64 0, i32 0
  %".18" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".17"
  %".19" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".18", %"struct.LinkedNode"** %".19"
  %".21" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 7
  %".22" = load i64 (%"struct.LinkedNode"*)*, i64 (%"struct.LinkedNode"*)** %".21"
  %".23" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".24" = call i64 %".22"(%"struct.LinkedNode"* %".23")
  %".25" = add i64 1, %".24"
  ret i64 %".25"
}

define %"struct.LinkedNode"* @"append469255175066110123140385251891312"(%"struct.LinkedNode"* %".1", %"struct.LinkedNode"* %".2")
{
.4:
  %".5" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".1", %"struct.LinkedNode"** %".5"
  %".7" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".2", %"struct.LinkedNode"** %".7"
  %".9" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".5"
  %".10" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".9", %"struct.LinkedNode"** %".10"
  %".12" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".9", i64 0, i32 6
  %".13" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".12"
  %".14" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".10"
  %".15" = call %"struct.LinkedNode"* %".13"(%"struct.LinkedNode"* %".14")
  %".16" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".15", %"struct.LinkedNode"** %".16"
  %".18" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".7"
  %".19" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".16"
  %".20" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".19", i64 0, i32 0
  store %"struct.LinkedNode"* %".18", %"struct.LinkedNode"** %".20"
  %".22" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".7"
  ret %"struct.LinkedNode"* %".22"
}

define %"struct.LinkedNode"* @"print3391917900011564653140385253288176"(%"struct.LinkedNode"* %".1")
{
.3:
  %".4" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".1", %"struct.LinkedNode"** %".4"
  %".6" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".7" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".8" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".7", i64 0, i32 1
  %".9" = load i8*, i8** %".8"
  %".10" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".11" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".10", i64 0, i32 2
  %".12" = load i64, i64* %".11"
  %".13" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".14" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".13", i64 0, i32 3
  %".15" = load i64, i64* %".14"
  %".16" = call i64 (i8*, ...) @"printf"(i8* getelementptr ([46 x i8], [46 x i8]* @".1", i64 0, i64 0), %"struct.LinkedNode"* %".6", i8* %".9", i64 %".12", i64 %".15")
  %".17" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  ret %"struct.LinkedNode"* %".17"
}

define %"struct.LinkedNode"* @"printAll5412683947079684783140385252328784"(%"struct.LinkedNode"* %".1")
{
.3:
  %".4" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".1", %"struct.LinkedNode"** %".4"
  %".6" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".7" = ptrtoint %"struct.LinkedNode"* %".6" to i64
  %".8" = icmp eq i64 %".7", 0
  %".9" = select  i1 %".8", i64 1, i64 0
  %".10" = icmp eq i64 %".9", 1
  br i1 %".10", label %".3.if", label %".3.endif"
.3.if:
  %".12" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  ret %"struct.LinkedNode"* %".12"
.3.endif:
  %".14" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".15" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".14", %"struct.LinkedNode"** %".15"
  br label %".17"
.17:
  %".21" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".15"
  %".22" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".21", %"struct.LinkedNode"** %".22"
  %".24" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".21", i64 0, i32 5
  %".25" = load i64 (%"struct.LinkedNode"*)*, i64 (%"struct.LinkedNode"*)** %".24"
  %".26" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".22"
  %".27" = call i64 %".25"(%"struct.LinkedNode"* %".26")
  %".28" = icmp eq i64 %".27", 0
  %".29" = select  i1 %".28", i64 1, i64 0
  %".30" = icmp eq i64 %".29", 1
  br i1 %".30", label %".19", label %".18"
.18:
  %".44" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".15"
  %".45" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".44", %"struct.LinkedNode"** %".45"
  %".47" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".44", i64 0, i32 9
  %".48" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".47"
  %".49" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".45"
  %".50" = call %"struct.LinkedNode"* %".48"(%"struct.LinkedNode"* %".49")
  %".51" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  ret %"struct.LinkedNode"* %".51"
.19:
  %".32" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".15"
  %".33" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".32", %"struct.LinkedNode"** %".33"
  %".35" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".32", i64 0, i32 9
  %".36" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".35"
  %".37" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".33"
  %".38" = call %"struct.LinkedNode"* %".36"(%"struct.LinkedNode"* %".37")
  %".39" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".15"
  %".40" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".39", i64 0, i32 0
  %".41" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".40"
  store %"struct.LinkedNode"* %".41", %"struct.LinkedNode"** %".15"
  br label %".17"
}

define %"struct.LinkedNode"* @"fromElementPointer1783074740778926399140385255390464"(%"struct.LinkedNode"* %".1", i8* %".2")
{
.4:
  %".5" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".1", %"struct.LinkedNode"** %".5"
  %".7" = alloca i8*
  store i8* %".2", i8** %".7"
  %".9" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".5"
  %".10" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".9", %"struct.LinkedNode"** %".10"
  br label %".12"
.12:
  %".16" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".10"
  %".17" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".16", %"struct.LinkedNode"** %".17"
  %".19" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".16", i64 0, i32 5
  %".20" = load i64 (%"struct.LinkedNode"*)*, i64 (%"struct.LinkedNode"*)** %".19"
  %".21" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".17"
  %".22" = call i64 %".20"(%"struct.LinkedNode"* %".21")
  %".23" = icmp eq i64 %".22", 0
  %".24" = select  i1 %".23", i64 1, i64 0
  %".25" = icmp eq i64 %".24", 1
  br i1 %".25", label %".14", label %".13"
.13:
  %".44" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".10"
  %".45" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".44", i64 0, i32 1
  %".46" = load i8*, i8** %".45"
  %".47" = ptrtoint i8* %".46" to i64
  %".48" = load i8*, i8** %".7"
  %".49" = ptrtoint i8* %".48" to i64
  %".50" = icmp eq i64 %".47", %".49"
  %".51" = select  i1 %".50", i64 1, i64 0
  %".52" = icmp eq i64 %".51", 1
  br i1 %".52", label %".13.if", label %".13.endif"
.14:
  %".27" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".10"
  %".28" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".27", i64 0, i32 1
  %".29" = load i8*, i8** %".28"
  %".30" = ptrtoint i8* %".29" to i64
  %".31" = load i8*, i8** %".7"
  %".32" = ptrtoint i8* %".31" to i64
  %".33" = icmp eq i64 %".30", %".32"
  %".34" = select  i1 %".33", i64 1, i64 0
  %".35" = icmp eq i64 %".34", 1
  br i1 %".35", label %".14.if", label %".14.endif"
.14.if:
  %".37" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".10"
  ret %"struct.LinkedNode"* %".37"
.14.endif:
  %".39" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".10"
  %".40" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".39", i64 0, i32 0
  %".41" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".40"
  store %"struct.LinkedNode"* %".41", %"struct.LinkedNode"** %".10"
  br label %".12"
.13.if:
  %".54" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".10"
  ret %"struct.LinkedNode"* %".54"
.13.endif:
  %".56" = inttoptr i64 0 to %"struct.LinkedNode"*
  ret %"struct.LinkedNode"* %".56"
}

define void @"end6481428791113684835140385254193184"(%"struct.LinkedNode"* %".1")
{
.3:
  %".4" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".1", %"struct.LinkedNode"** %".4"
  %".6" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".7" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".6", i64 0, i32 1
  %".8" = load i8*, i8** %".7"
  %".9" = ptrtoint i8* %".8" to i64
  %".10" = icmp ne i64 %".9", 0
  %".11" = select  i1 %".10", i64 1, i64 0
  %".12" = icmp eq i64 %".11", 1
  br i1 %".12", label %".3.if", label %".3.endif"
.3.if:
  %".14" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".15" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".14", i64 0, i32 1
  %".16" = load i8*, i8** %".15"
  call void @"free"(i8* %".16")
  br label %".3.endif"
.3.endif:
  %".19" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".20" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".19", i64 0, i32 0
  %".21" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".20"
  %".22" = ptrtoint %"struct.LinkedNode"* %".21" to i64
  %".23" = icmp ne i64 %".22", 0
  %".24" = select  i1 %".23", i64 1, i64 0
  %".25" = icmp eq i64 %".24", 1
  br i1 %".25", label %".3.endif.if", label %".3.endif.endif"
.3.endif.if:
  %".27" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".28" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".27", i64 0, i32 0
  %".29" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".28"
  %".30" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".29", %"struct.LinkedNode"** %".30"
  %".32" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".29", i64 0, i32 12
  %".33" = load void (%"struct.LinkedNode"*)*, void (%"struct.LinkedNode"*)** %".32"
  %".34" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".30"
  call void %".33"(%"struct.LinkedNode"* %".34")
  br label %".3.endif.endif"
.3.endif.endif:
  %".37" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".4"
  %".38" = bitcast %"struct.LinkedNode"* %".37" to i8*
  call void @"free"(i8* %".38")
  ret void
}

define i8* @"memcpyn140385253191072"(i8* %".1", i8* %".2", i64 %".3", i64 %".4")
{
.6:
  %".7" = alloca i8*
  store i8* %".1", i8** %".7"
  %".9" = alloca i8*
  store i8* %".2", i8** %".9"
  %".11" = alloca i64
  store i64 %".3", i64* %".11"
  %".13" = alloca i64
  store i64 %".4", i64* %".13"
  %".15" = alloca i64
  store i64 0, i64* %".15"
  br label %".17"
.17:
  %".21" = load i64, i64* %".15"
  %".22" = load i64, i64* %".13"
  %".23" = icmp slt i64 %".21", %".22"
  %".24" = select  i1 %".23", i64 1, i64 0
  %".25" = icmp eq i64 %".24", 1
  br i1 %".25", label %".19", label %".18"
.18:
  %".41" = load i8*, i8** %".7"
  ret i8* %".41"
.19:
  %".27" = load i8*, i8** %".7"
  %".28" = ptrtoint i8* %".27" to i64
  %".29" = load i64, i64* %".11"
  %".30" = load i64, i64* %".15"
  %".31" = mul i64 %".29", %".30"
  %".32" = add i64 %".28", %".31"
  %".33" = inttoptr i64 %".32" to i8*
  %".34" = load i8*, i8** %".9"
  %".35" = load i64, i64* %".11"
  %".36" = call i8* @"memcpy"(i8* %".33", i8* %".34", i64 %".35")
  %".37" = load i64, i64* %".15"
  %".38" = add i64 %".37", 1
  store i64 %".38", i64* %".15"
  br label %".17"
}

define %"struct.GC"* @"start7835992373913572580140385256715312"(%"struct.GC"* %".1")
{
.3:
  %".4" = alloca %"struct.GC"*
  store %"struct.GC"* %".1", %"struct.GC"** %".4"
  %".6" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".7" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".8" = getelementptr %"struct.GC", %"struct.GC"* %".7", i64 0, i32 0
  store %"struct.LinkedNode"* %".6", %"struct.LinkedNode"** %".8"
  %".10" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".11" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".12" = getelementptr %"struct.GC", %"struct.GC"* %".11", i64 0, i32 1
  store %"struct.LinkedNode"* %".10", %"struct.LinkedNode"** %".12"
  %".14" = load %"struct.GC"*, %"struct.GC"** %".4"
  ret %"struct.GC"* %".14"
}

define i8* @"push6196927396915817214140385256710320"(%"struct.GC"* %".1", i8* %".2", i64 %".3")
{
.5:
  %".6" = alloca %"struct.GC"*
  store %"struct.GC"* %".1", %"struct.GC"** %".6"
  %".8" = alloca i8*
  store i8* %".2", i8** %".8"
  %".10" = alloca i64
  store i64 %".3", i64* %".10"
  %".12" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140385250703392"
  %".13" = load i8* (i64)*, i8* (i64)** @"__malloc140385250699696"
  %".14" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".15" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".14", i32 1
  %".16" = ptrtoint %"struct.LinkedNode"* %".15" to i64
  %".17" = call i8* %".13"(i64 %".16")
  %".18" = alloca %"struct.LinkedNode"
  %".19" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 4
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)* @"start5751983272486680366140385253942144", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".19"
  %".21" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 5
  store i64 (%"struct.LinkedNode"*)* @"isLast5536074550656775930140385253936288", i64 (%"struct.LinkedNode"*)** %".21"
  %".23" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 6
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"getLast3120310538166611506140385253944880", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".23"
  %".25" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 7
  store i64 (%"struct.LinkedNode"*)* @"size3858513429958943938140385251897072", i64 (%"struct.LinkedNode"*)** %".25"
  %".27" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 8
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)* @"append469255175066110123140385251891312", %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".27"
  %".29" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 9
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"print3391917900011564653140385253288176", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".29"
  %".31" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 10
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"printAll5412683947079684783140385252328784", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".31"
  %".33" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 11
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)* @"fromElementPointer1783074740778926399140385255390464", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".33"
  %".35" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 12
  store void (%"struct.LinkedNode"*)* @"end6481428791113684835140385254193184", void (%"struct.LinkedNode"*)** %".35"
  %".37" = bitcast %"struct.LinkedNode"* %".18" to i8*
  %".38" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".39" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".38", i32 1
  %".40" = ptrtoint %"struct.LinkedNode"* %".39" to i64
  %".41" = call i8* %".12"(i8* %".17", i8* %".37", i64 %".40")
  %".42" = bitcast i8* %".41" to %"struct.LinkedNode"*
  %".43" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".42", %"struct.LinkedNode"** %".43"
  %".45" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".42", i64 0, i32 4
  %".46" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".45"
  %".47" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".43"
  %".48" = load i8*, i8** %".8"
  %".49" = load i64, i64* %".10"
  %".50" = call %"struct.LinkedNode"* %".46"(%"struct.LinkedNode"* %".47", i8* %".48", i64 %".49")
  %".51" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".50", %"struct.LinkedNode"** %".51"
  %".53" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140385250703392"
  %".54" = load i8* (i64)*, i8* (i64)** @"__malloc140385250699696"
  %".55" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".56" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".55", i32 1
  %".57" = ptrtoint %"struct.LinkedNode"* %".56" to i64
  %".58" = call i8* %".54"(i64 %".57")
  %".59" = alloca %"struct.LinkedNode"
  %".60" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 4
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)* @"start5751983272486680366140385253942144", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".60"
  %".62" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 5
  store i64 (%"struct.LinkedNode"*)* @"isLast5536074550656775930140385253936288", i64 (%"struct.LinkedNode"*)** %".62"
  %".64" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 6
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"getLast3120310538166611506140385253944880", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".64"
  %".66" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 7
  store i64 (%"struct.LinkedNode"*)* @"size3858513429958943938140385251897072", i64 (%"struct.LinkedNode"*)** %".66"
  %".68" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 8
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)* @"append469255175066110123140385251891312", %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".68"
  %".70" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 9
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"print3391917900011564653140385253288176", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".70"
  %".72" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 10
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"printAll5412683947079684783140385252328784", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".72"
  %".74" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 11
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)* @"fromElementPointer1783074740778926399140385255390464", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".74"
  %".76" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 12
  store void (%"struct.LinkedNode"*)* @"end6481428791113684835140385254193184", void (%"struct.LinkedNode"*)** %".76"
  %".78" = bitcast %"struct.LinkedNode"* %".59" to i8*
  %".79" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".80" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".79", i32 1
  %".81" = ptrtoint %"struct.LinkedNode"* %".80" to i64
  %".82" = call i8* %".53"(i8* %".58", i8* %".78", i64 %".81")
  %".83" = bitcast i8* %".82" to %"struct.LinkedNode"*
  %".84" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".83", %"struct.LinkedNode"** %".84"
  %".86" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".83", i64 0, i32 4
  %".87" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".86"
  %".88" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".84"
  %".89" = load i8*, i8** %".8"
  %".90" = load i64, i64* %".10"
  %".91" = call %"struct.LinkedNode"* %".87"(%"struct.LinkedNode"* %".88", i8* %".89", i64 %".90")
  %".92" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".91", %"struct.LinkedNode"** %".92"
  %".94" = load %"struct.GC"*, %"struct.GC"** %".6"
  %".95" = getelementptr %"struct.GC", %"struct.GC"* %".94", i64 0, i32 0
  %".96" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".95"
  %".97" = ptrtoint %"struct.LinkedNode"* %".96" to i64
  %".98" = icmp eq i64 %".97", 0
  %".99" = select  i1 %".98", i64 1, i64 0
  %".100" = icmp eq i64 %".99", 1
  br i1 %".100", label %".5.if", label %".5.endif"
.5.if:
  %".102" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".51"
  %".103" = load %"struct.GC"*, %"struct.GC"** %".6"
  %".104" = getelementptr %"struct.GC", %"struct.GC"* %".103", i64 0, i32 0
  store %"struct.LinkedNode"* %".102", %"struct.LinkedNode"** %".104"
  %".106" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".92"
  %".107" = load %"struct.GC"*, %"struct.GC"** %".6"
  %".108" = getelementptr %"struct.GC", %"struct.GC"* %".107", i64 0, i32 1
  store %"struct.LinkedNode"* %".106", %"struct.LinkedNode"** %".108"
  %".110" = load i8*, i8** %".8"
  ret i8* %".110"
.5.endif:
  %".112" = load %"struct.GC"*, %"struct.GC"** %".6"
  %".113" = getelementptr %"struct.GC", %"struct.GC"* %".112", i64 0, i32 0
  %".114" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".113"
  %".115" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".114", %"struct.LinkedNode"** %".115"
  %".117" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".114", i64 0, i32 8
  %".118" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".117"
  %".119" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".115"
  %".120" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".51"
  %".121" = call %"struct.LinkedNode"* %".118"(%"struct.LinkedNode"* %".119", %"struct.LinkedNode"* %".120")
  %".122" = load %"struct.GC"*, %"struct.GC"** %".6"
  %".123" = getelementptr %"struct.GC", %"struct.GC"* %".122", i64 0, i32 1
  %".124" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".123"
  %".125" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".124", %"struct.LinkedNode"** %".125"
  %".127" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".124", i64 0, i32 8
  %".128" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".127"
  %".129" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".125"
  %".130" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".92"
  %".131" = call %"struct.LinkedNode"* %".128"(%"struct.LinkedNode"* %".129", %"struct.LinkedNode"* %".130")
  %".132" = load i8*, i8** %".8"
  ret i8* %".132"
}

define i8* @"pushNoRoot3847600348900564826140385255537920"(%"struct.GC"* %".1", i8* %".2", i64 %".3")
{
.5:
  %".6" = alloca %"struct.GC"*
  store %"struct.GC"* %".1", %"struct.GC"** %".6"
  %".8" = alloca i8*
  store i8* %".2", i8** %".8"
  %".10" = alloca i64
  store i64 %".3", i64* %".10"
  %".12" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140385250703392"
  %".13" = load i8* (i64)*, i8* (i64)** @"__malloc140385250699696"
  %".14" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".15" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".14", i32 1
  %".16" = ptrtoint %"struct.LinkedNode"* %".15" to i64
  %".17" = call i8* %".13"(i64 %".16")
  %".18" = alloca %"struct.LinkedNode"
  %".19" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 4
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)* @"start5751983272486680366140385253942144", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".19"
  %".21" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 5
  store i64 (%"struct.LinkedNode"*)* @"isLast5536074550656775930140385253936288", i64 (%"struct.LinkedNode"*)** %".21"
  %".23" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 6
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"getLast3120310538166611506140385253944880", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".23"
  %".25" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 7
  store i64 (%"struct.LinkedNode"*)* @"size3858513429958943938140385251897072", i64 (%"struct.LinkedNode"*)** %".25"
  %".27" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 8
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)* @"append469255175066110123140385251891312", %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".27"
  %".29" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 9
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"print3391917900011564653140385253288176", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".29"
  %".31" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 10
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"printAll5412683947079684783140385252328784", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".31"
  %".33" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 11
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)* @"fromElementPointer1783074740778926399140385255390464", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".33"
  %".35" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 12
  store void (%"struct.LinkedNode"*)* @"end6481428791113684835140385254193184", void (%"struct.LinkedNode"*)** %".35"
  %".37" = bitcast %"struct.LinkedNode"* %".18" to i8*
  %".38" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".39" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".38", i32 1
  %".40" = ptrtoint %"struct.LinkedNode"* %".39" to i64
  %".41" = call i8* %".12"(i8* %".17", i8* %".37", i64 %".40")
  %".42" = bitcast i8* %".41" to %"struct.LinkedNode"*
  %".43" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".42", %"struct.LinkedNode"** %".43"
  %".45" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".42", i64 0, i32 4
  %".46" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".45"
  %".47" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".43"
  %".48" = load i8*, i8** %".8"
  %".49" = load i64, i64* %".10"
  %".50" = call %"struct.LinkedNode"* %".46"(%"struct.LinkedNode"* %".47", i8* %".48", i64 %".49")
  %".51" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".50", %"struct.LinkedNode"** %".51"
  %".53" = load %"struct.GC"*, %"struct.GC"** %".6"
  %".54" = getelementptr %"struct.GC", %"struct.GC"* %".53", i64 0, i32 0
  %".55" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".54"
  %".56" = ptrtoint %"struct.LinkedNode"* %".55" to i64
  %".57" = icmp eq i64 %".56", 0
  %".58" = select  i1 %".57", i64 1, i64 0
  %".59" = icmp eq i64 %".58", 1
  br i1 %".59", label %".5.if", label %".5.endif"
.5.if:
  %".61" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".51"
  %".62" = load %"struct.GC"*, %"struct.GC"** %".6"
  %".63" = getelementptr %"struct.GC", %"struct.GC"* %".62", i64 0, i32 0
  store %"struct.LinkedNode"* %".61", %"struct.LinkedNode"** %".63"
  %".65" = load i8*, i8** %".8"
  ret i8* %".65"
.5.endif:
  %".67" = load %"struct.GC"*, %"struct.GC"** %".6"
  %".68" = getelementptr %"struct.GC", %"struct.GC"* %".67", i64 0, i32 0
  %".69" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".68"
  %".70" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".69", %"struct.LinkedNode"** %".70"
  %".72" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".69", i64 0, i32 8
  %".73" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".72"
  %".74" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".70"
  %".75" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".51"
  %".76" = call %"struct.LinkedNode"* %".73"(%"struct.LinkedNode"* %".74", %"struct.LinkedNode"* %".75")
  %".77" = load i8*, i8** %".8"
  ret i8* %".77"
}

define %"struct.GC"* @"pop4268654653910679871140385252978848"(%"struct.GC"* %".1")
{
.3:
  %".4" = alloca %"struct.GC"*
  store %"struct.GC"* %".1", %"struct.GC"** %".4"
  %".6" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".7" = getelementptr %"struct.GC", %"struct.GC"* %".6", i64 0, i32 1
  %".8" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".7"
  %".9" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".8", %"struct.LinkedNode"** %".9"
  %".11" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".8", i64 0, i32 7
  %".12" = load i64 (%"struct.LinkedNode"*)*, i64 (%"struct.LinkedNode"*)** %".11"
  %".13" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".9"
  %".14" = call i64 %".12"(%"struct.LinkedNode"* %".13")
  %".15" = alloca i64
  store i64 %".14", i64* %".15"
  %".17" = load i64, i64* %".15"
  %".18" = icmp eq i64 %".17", 1
  %".19" = select  i1 %".18", i64 1, i64 0
  %".20" = icmp eq i64 %".19", 1
  br i1 %".20", label %".3.if", label %".3.endif"
.3.if:
  %".22" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".23" = getelementptr %"struct.GC", %"struct.GC"* %".22", i64 0, i32 1
  %".24" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".23"
  %".25" = bitcast %"struct.LinkedNode"* %".24" to i8*
  call void @"free"(i8* %".25")
  %".27" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".28" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".29" = getelementptr %"struct.GC", %"struct.GC"* %".28", i64 0, i32 1
  store %"struct.LinkedNode"* %".27", %"struct.LinkedNode"** %".29"
  %".31" = load %"struct.GC"*, %"struct.GC"** %".4"
  ret %"struct.GC"* %".31"
.3.endif:
  %".33" = load i64, i64* %".15"
  %".34" = icmp sge i64 %".33", 2
  %".35" = select  i1 %".34", i64 1, i64 0
  %".36" = icmp eq i64 %".35", 1
  br i1 %".36", label %".3.endif.if", label %".3.endif.endif"
.3.endif.if:
  %".38" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".39" = getelementptr %"struct.GC", %"struct.GC"* %".38", i64 0, i32 1
  %".40" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".39"
  %".41" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".40", %"struct.LinkedNode"** %".41"
  br label %".43"
.3.endif.endif:
  %".73" = load %"struct.GC"*, %"struct.GC"** %".4"
  ret %"struct.GC"* %".73"
.43:
  %".47" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".41"
  %".48" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".47", i64 0, i32 0
  %".49" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".48"
  %".50" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".49", i64 0, i32 0
  %".51" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".50"
  %".52" = ptrtoint %"struct.LinkedNode"* %".51" to i64
  %".53" = icmp ne i64 %".52", 0
  %".54" = select  i1 %".53", i64 1, i64 0
  %".55" = icmp eq i64 %".54", 1
  br i1 %".55", label %".45", label %".44"
.44:
  %".62" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".41"
  %".63" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".62", i64 0, i32 0
  %".64" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".63"
  %".65" = bitcast %"struct.LinkedNode"* %".64" to i8*
  call void @"free"(i8* %".65")
  %".67" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".68" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".41"
  %".69" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".68", i64 0, i32 0
  store %"struct.LinkedNode"* %".67", %"struct.LinkedNode"** %".69"
  %".71" = load %"struct.GC"*, %"struct.GC"** %".4"
  ret %"struct.GC"* %".71"
.45:
  %".57" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".41"
  %".58" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".57", i64 0, i32 0
  %".59" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".58"
  store %"struct.LinkedNode"* %".59", %"struct.LinkedNode"** %".41"
  br label %".43"
}

define %"struct.GC"* @"mark_root7785180052072167530140385255689808"(%"struct.GC"* %".1", i8* %".2")
{
.4:
  %".5" = alloca %"struct.GC"*
  store %"struct.GC"* %".1", %"struct.GC"** %".5"
  %".7" = alloca i8*
  store i8* %".2", i8** %".7"
  %".9" = load %"struct.GC"*, %"struct.GC"** %".5"
  %".10" = getelementptr %"struct.GC", %"struct.GC"* %".9", i64 0, i32 0
  %".11" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".10"
  %".12" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".11", %"struct.LinkedNode"** %".12"
  %".14" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".11", i64 0, i32 11
  %".15" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".14"
  %".16" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".12"
  %".17" = load i8*, i8** %".7"
  %".18" = call %"struct.LinkedNode"* %".15"(%"struct.LinkedNode"* %".16", i8* %".17")
  %".19" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".18", %"struct.LinkedNode"** %".19"
  %".21" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".22" = ptrtoint %"struct.LinkedNode"* %".21" to i64
  %".23" = icmp ne i64 %".22", 0
  %".24" = select  i1 %".23", i64 1, i64 0
  %".25" = icmp eq i64 %".24", 1
  br i1 %".25", label %".4.if", label %".4.endif"
.4.if:
  %".27" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".28" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".27", i64 0, i32 3
  store i64 1, i64* %".28"
  %".30" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".31" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".30", i64 0, i32 1
  %".32" = load i8*, i8** %".31"
  %".33" = ptrtoint i8* %".32" to i64
  %".34" = alloca i64
  store i64 %".33", i64* %".34"
  %".36" = load i64, i64* %".34"
  %".37" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".38" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".37", i64 0, i32 2
  %".39" = load i64, i64* %".38"
  %".40" = add i64 %".36", %".39"
  %".41" = alloca i64
  store i64 %".40", i64* %".41"
  br label %".43"
.4.endif:
  %".99" = load %"struct.GC"*, %"struct.GC"** %".5"
  ret %"struct.GC"* %".99"
.43:
  %".47" = load i64, i64* %".34"
  %".48" = load i64, i64* %".41"
  %".49" = icmp slt i64 %".47", %".48"
  %".50" = select  i1 %".49", i64 1, i64 0
  %".51" = icmp eq i64 %".50", 1
  br i1 %".51", label %".45", label %".44"
.44:
  br label %".4.endif"
.45:
  %".53" = load %"struct.GC"*, %"struct.GC"** %".5"
  %".54" = getelementptr %"struct.GC", %"struct.GC"* %".53", i64 0, i32 0
  %".55" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".54"
  %".56" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".55", %"struct.LinkedNode"** %".56"
  %".58" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".55", i64 0, i32 11
  %".59" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".58"
  %".60" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".56"
  %".61" = load i64, i64* %".34"
  %".62" = inttoptr i64 %".61" to i8**
  %".63" = getelementptr i8*, i8** %".62", i64 0
  %".64" = load i8*, i8** %".63"
  %".65" = call %"struct.LinkedNode"* %".59"(%"struct.LinkedNode"* %".60", i8* %".64")
  %".66" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".65", %"struct.LinkedNode"** %".66"
  %".68" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".66"
  %".69" = ptrtoint %"struct.LinkedNode"* %".68" to i64
  %".70" = icmp ne i64 %".69", 0
  %".71" = select  i1 %".70", i64 1, i64 0
  %".72" = icmp eq i64 %".71", 1
  br i1 %".72", label %".45.if", label %".45.endif"
.45.if:
  %".74" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".66"
  %".75" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".74", i64 0, i32 3
  %".76" = load i64, i64* %".75"
  %".77" = icmp eq i64 %".76", 0
  %".78" = select  i1 %".77", i64 1, i64 0
  %".79" = icmp eq i64 %".78", 1
  br i1 %".79", label %".45.if.if", label %".45.if.endif"
.45.endif:
  %".94" = load i64, i64* %".34"
  %".95" = add i64 %".94", 8
  store i64 %".95", i64* %".34"
  br label %".43"
.45.if.if:
  %".81" = load %"struct.GC"*, %"struct.GC"** %".5"
  %".82" = alloca %"struct.GC"*
  store %"struct.GC"* %".81", %"struct.GC"** %".82"
  %".84" = getelementptr %"struct.GC", %"struct.GC"* %".81", i64 0, i32 6
  %".85" = load %"struct.GC"* (%"struct.GC"*, i8*)*, %"struct.GC"* (%"struct.GC"*, i8*)** %".84"
  %".86" = load %"struct.GC"*, %"struct.GC"** %".82"
  %".87" = load i64, i64* %".34"
  %".88" = inttoptr i64 %".87" to i8**
  %".89" = getelementptr i8*, i8** %".88", i64 0
  %".90" = load i8*, i8** %".89"
  %".91" = call %"struct.GC"* %".85"(%"struct.GC"* %".86", i8* %".90")
  br label %".45.if.endif"
.45.if.endif:
  br label %".45.endif"
}

define %"struct.GC"* @"mark3850657141341536777140385253218128"(%"struct.GC"* %".1")
{
.3:
  %".4" = alloca %"struct.GC"*
  store %"struct.GC"* %".1", %"struct.GC"** %".4"
  %".6" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".7" = getelementptr %"struct.GC", %"struct.GC"* %".6", i64 0, i32 1
  %".8" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".7"
  %".9" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".8", %"struct.LinkedNode"** %".9"
  br label %".11"
.11:
  %".15" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".9"
  %".16" = ptrtoint %"struct.LinkedNode"* %".15" to i64
  %".17" = icmp ne i64 %".16", 0
  %".18" = select  i1 %".17", i64 1, i64 0
  %".19" = icmp eq i64 %".18", 1
  br i1 %".19", label %".13", label %".12"
.12:
  %".36" = call i64 (i8*, ...) @"printf"(i8* getelementptr ([37 x i8], [37 x i8]* @".2", i64 0, i64 0))
  %".37" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".38" = getelementptr %"struct.GC", %"struct.GC"* %".37", i64 0, i32 0
  %".39" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".38"
  %".40" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".39", %"struct.LinkedNode"** %".40"
  %".42" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".39", i64 0, i32 10
  %".43" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".42"
  %".44" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".40"
  %".45" = call %"struct.LinkedNode"* %".43"(%"struct.LinkedNode"* %".44")
  %".46" = load %"struct.GC"*, %"struct.GC"** %".4"
  ret %"struct.GC"* %".46"
.13:
  %".21" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".22" = alloca %"struct.GC"*
  store %"struct.GC"* %".21", %"struct.GC"** %".22"
  %".24" = getelementptr %"struct.GC", %"struct.GC"* %".21", i64 0, i32 6
  %".25" = load %"struct.GC"* (%"struct.GC"*, i8*)*, %"struct.GC"* (%"struct.GC"*, i8*)** %".24"
  %".26" = load %"struct.GC"*, %"struct.GC"** %".22"
  %".27" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".9"
  %".28" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".27", i64 0, i32 1
  %".29" = load i8*, i8** %".28"
  %".30" = call %"struct.GC"* %".25"(%"struct.GC"* %".26", i8* %".29")
  %".31" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".9"
  %".32" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".31", i64 0, i32 0
  %".33" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".32"
  store %"struct.LinkedNode"* %".33", %"struct.LinkedNode"** %".9"
  br label %".11"
}

define %"struct.GC"* @"unmark8713185513450541210140385244202368"(%"struct.GC"* %".1")
{
.3:
  %".4" = alloca %"struct.GC"*
  store %"struct.GC"* %".1", %"struct.GC"** %".4"
  %".6" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".7" = getelementptr %"struct.GC", %"struct.GC"* %".6", i64 0, i32 0
  %".8" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".7"
  %".9" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".8", %"struct.LinkedNode"** %".9"
  br label %".11"
.11:
  %".15" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".9"
  %".16" = ptrtoint %"struct.LinkedNode"* %".15" to i64
  %".17" = icmp ne i64 %".16", 0
  %".18" = select  i1 %".17", i64 1, i64 0
  %".19" = icmp eq i64 %".18", 1
  br i1 %".19", label %".13", label %".12"
.12:
  %".29" = load %"struct.GC"*, %"struct.GC"** %".4"
  ret %"struct.GC"* %".29"
.13:
  %".21" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".9"
  %".22" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".21", i64 0, i32 3
  store i64 0, i64* %".22"
  %".24" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".9"
  %".25" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".24", i64 0, i32 0
  %".26" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".25"
  store %"struct.LinkedNode"* %".26", %"struct.LinkedNode"** %".9"
  br label %".11"
}

define %"struct.GC"* @"sweep8665498114076620315140385244216768"(%"struct.GC"* %".1")
{
.3:
  %".4" = alloca %"struct.GC"*
  store %"struct.GC"* %".1", %"struct.GC"** %".4"
  %".6" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".7" = getelementptr %"struct.GC", %"struct.GC"* %".6", i64 0, i32 0
  %".8" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".7"
  %".9" = ptrtoint %"struct.LinkedNode"* %".8" to i64
  %".10" = icmp eq i64 %".9", 0
  %".11" = select  i1 %".10", i64 1, i64 0
  %".12" = icmp eq i64 %".11", 1
  br i1 %".12", label %".3.if", label %".3.endif"
.3.if:
  %".14" = load %"struct.GC"*, %"struct.GC"** %".4"
  ret %"struct.GC"* %".14"
.3.endif:
  %".16" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".17" = getelementptr %"struct.GC", %"struct.GC"* %".16", i64 0, i32 0
  %".18" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".17"
  %".19" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".18", %"struct.LinkedNode"** %".19"
  %".21" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".22" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".21", %"struct.LinkedNode"** %".22"
  %".24" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".25" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".24", %"struct.LinkedNode"** %".25"
  br label %".27"
.27:
  %".31" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".32" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".31", %"struct.LinkedNode"** %".32"
  %".34" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".31", i64 0, i32 5
  %".35" = load i64 (%"struct.LinkedNode"*)*, i64 (%"struct.LinkedNode"*)** %".34"
  %".36" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".32"
  %".37" = call i64 %".35"(%"struct.LinkedNode"* %".36")
  %".38" = icmp eq i64 %".37", 0
  %".39" = select  i1 %".38", i64 1, i64 0
  %".40" = icmp eq i64 %".39", 1
  br i1 %".40", label %".29", label %".28"
.28:
  %".170" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140385250703392"
  %".171" = load i8* (i64)*, i8* (i64)** @"__malloc140385250699696"
  %".172" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".173" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".172", i32 1
  %".174" = ptrtoint %"struct.LinkedNode"* %".173" to i64
  %".175" = call i8* %".171"(i64 %".174")
  %".176" = alloca %"struct.LinkedNode"
  %".177" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 4
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)* @"start5751983272486680366140385253942144", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".177"
  %".179" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 5
  store i64 (%"struct.LinkedNode"*)* @"isLast5536074550656775930140385253936288", i64 (%"struct.LinkedNode"*)** %".179"
  %".181" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 6
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"getLast3120310538166611506140385253944880", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".181"
  %".183" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 7
  store i64 (%"struct.LinkedNode"*)* @"size3858513429958943938140385251897072", i64 (%"struct.LinkedNode"*)** %".183"
  %".185" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 8
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)* @"append469255175066110123140385251891312", %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".185"
  %".187" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 9
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"print3391917900011564653140385253288176", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".187"
  %".189" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 10
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"printAll5412683947079684783140385252328784", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".189"
  %".191" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 11
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)* @"fromElementPointer1783074740778926399140385255390464", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".191"
  %".193" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 12
  store void (%"struct.LinkedNode"*)* @"end6481428791113684835140385254193184", void (%"struct.LinkedNode"*)** %".193"
  %".195" = bitcast %"struct.LinkedNode"* %".176" to i8*
  %".196" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".197" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".196", i32 1
  %".198" = ptrtoint %"struct.LinkedNode"* %".197" to i64
  %".199" = call i8* %".170"(i8* %".175", i8* %".195", i64 %".198")
  %".200" = bitcast i8* %".199" to %"struct.LinkedNode"*
  %".201" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".200", %"struct.LinkedNode"** %".201"
  %".203" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".200", i64 0, i32 4
  %".204" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".203"
  %".205" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".201"
  %".206" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".207" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".206", i64 0, i32 1
  %".208" = load i8*, i8** %".207"
  %".209" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".210" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".209", i64 0, i32 2
  %".211" = load i64, i64* %".210"
  %".212" = call %"struct.LinkedNode"* %".204"(%"struct.LinkedNode"* %".205", i8* %".208", i64 %".211")
  %".213" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".212", %"struct.LinkedNode"** %".213"
  %".215" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".216" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".215", i64 0, i32 3
  %".217" = load i64, i64* %".216"
  %".218" = icmp eq i64 %".217", 1
  %".219" = select  i1 %".218", i64 1, i64 0
  %".220" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".22"
  %".221" = ptrtoint %"struct.LinkedNode"* %".220" to i64
  %".222" = icmp ne i64 %".221", 0
  %".223" = select  i1 %".222", i64 1, i64 0
  %".224" = mul i64 %".219", %".223"
  %".225" = icmp eq i64 %".224", 1
  br i1 %".225", label %".28.if", label %".28.endif"
.29:
  %".42" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140385250703392"
  %".43" = load i8* (i64)*, i8* (i64)** @"__malloc140385250699696"
  %".44" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".45" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".44", i32 1
  %".46" = ptrtoint %"struct.LinkedNode"* %".45" to i64
  %".47" = call i8* %".43"(i64 %".46")
  %".48" = alloca %"struct.LinkedNode"
  %".49" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 4
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)* @"start5751983272486680366140385253942144", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".49"
  %".51" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 5
  store i64 (%"struct.LinkedNode"*)* @"isLast5536074550656775930140385253936288", i64 (%"struct.LinkedNode"*)** %".51"
  %".53" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 6
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"getLast3120310538166611506140385253944880", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".53"
  %".55" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 7
  store i64 (%"struct.LinkedNode"*)* @"size3858513429958943938140385251897072", i64 (%"struct.LinkedNode"*)** %".55"
  %".57" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 8
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)* @"append469255175066110123140385251891312", %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".57"
  %".59" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 9
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"print3391917900011564653140385253288176", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".59"
  %".61" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 10
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"printAll5412683947079684783140385252328784", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".61"
  %".63" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 11
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)* @"fromElementPointer1783074740778926399140385255390464", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".63"
  %".65" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 12
  store void (%"struct.LinkedNode"*)* @"end6481428791113684835140385254193184", void (%"struct.LinkedNode"*)** %".65"
  %".67" = bitcast %"struct.LinkedNode"* %".48" to i8*
  %".68" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".69" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".68", i32 1
  %".70" = ptrtoint %"struct.LinkedNode"* %".69" to i64
  %".71" = call i8* %".42"(i8* %".47", i8* %".67", i64 %".70")
  %".72" = bitcast i8* %".71" to %"struct.LinkedNode"*
  %".73" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".72", %"struct.LinkedNode"** %".73"
  %".75" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".72", i64 0, i32 4
  %".76" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".75"
  %".77" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".73"
  %".78" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".79" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".78", i64 0, i32 1
  %".80" = load i8*, i8** %".79"
  %".81" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".82" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".81", i64 0, i32 2
  %".83" = load i64, i64* %".82"
  %".84" = call %"struct.LinkedNode"* %".76"(%"struct.LinkedNode"* %".77", i8* %".80", i64 %".83")
  %".85" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".84", %"struct.LinkedNode"** %".85"
  %".87" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".88" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".87", i64 0, i32 3
  %".89" = load i64, i64* %".88"
  %".90" = icmp eq i64 %".89", 1
  %".91" = select  i1 %".90", i64 1, i64 0
  %".92" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".22"
  %".93" = ptrtoint %"struct.LinkedNode"* %".92" to i64
  %".94" = icmp ne i64 %".93", 0
  %".95" = select  i1 %".94", i64 1, i64 0
  %".96" = mul i64 %".91", %".95"
  %".97" = icmp eq i64 %".96", 1
  br i1 %".97", label %".29.if", label %".29.endif"
.29.if:
  %".99" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".22"
  %".100" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".99", %"struct.LinkedNode"** %".100"
  %".102" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".99", i64 0, i32 8
  %".103" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".102"
  %".104" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".100"
  %".105" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".85"
  %".106" = call %"struct.LinkedNode"* %".103"(%"struct.LinkedNode"* %".104", %"struct.LinkedNode"* %".105")
  br label %".29.endif"
.29.endif:
  %".108" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".109" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".108", i64 0, i32 3
  %".110" = load i64, i64* %".109"
  %".111" = icmp eq i64 %".110", 1
  %".112" = select  i1 %".111", i64 1, i64 0
  %".113" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".22"
  %".114" = ptrtoint %"struct.LinkedNode"* %".113" to i64
  %".115" = icmp eq i64 %".114", 0
  %".116" = select  i1 %".115", i64 1, i64 0
  %".117" = mul i64 %".112", %".116"
  %".118" = icmp eq i64 %".117", 1
  br i1 %".118", label %".29.endif.if", label %".29.endif.endif"
.29.endif.if:
  %".120" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".85"
  store %"struct.LinkedNode"* %".120", %"struct.LinkedNode"** %".22"
  br label %".29.endif.endif"
.29.endif.endif:
  %".123" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".124" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".123", i64 0, i32 3
  %".125" = load i64, i64* %".124"
  %".126" = icmp eq i64 %".125", 0
  %".127" = select  i1 %".126", i64 1, i64 0
  %".128" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".25"
  %".129" = ptrtoint %"struct.LinkedNode"* %".128" to i64
  %".130" = icmp ne i64 %".129", 0
  %".131" = select  i1 %".130", i64 1, i64 0
  %".132" = mul i64 %".127", %".131"
  %".133" = icmp eq i64 %".132", 1
  br i1 %".133", label %".29.endif.endif.if", label %".29.endif.endif.endif"
.29.endif.endif.if:
  %".135" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".25"
  %".136" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".135", %"struct.LinkedNode"** %".136"
  %".138" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".135", i64 0, i32 8
  %".139" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".138"
  %".140" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".136"
  %".141" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".85"
  %".142" = call %"struct.LinkedNode"* %".139"(%"struct.LinkedNode"* %".140", %"struct.LinkedNode"* %".141")
  br label %".29.endif.endif.endif"
.29.endif.endif.endif:
  %".144" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".145" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".144", i64 0, i32 3
  %".146" = load i64, i64* %".145"
  %".147" = icmp eq i64 %".146", 0
  %".148" = select  i1 %".147", i64 1, i64 0
  %".149" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".25"
  %".150" = ptrtoint %"struct.LinkedNode"* %".149" to i64
  %".151" = icmp eq i64 %".150", 0
  %".152" = select  i1 %".151", i64 1, i64 0
  %".153" = mul i64 %".148", %".152"
  %".154" = icmp eq i64 %".153", 1
  br i1 %".154", label %".29.endif.endif.endif.if", label %".29.endif.endif.endif.endif"
.29.endif.endif.endif.if:
  %".156" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".85"
  store %"struct.LinkedNode"* %".156", %"struct.LinkedNode"** %".25"
  br label %".29.endif.endif.endif.endif"
.29.endif.endif.endif.endif:
  %".159" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".160" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".159", %"struct.LinkedNode"** %".160"
  %".162" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".163" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".162", i64 0, i32 0
  %".164" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".163"
  store %"struct.LinkedNode"* %".164", %"struct.LinkedNode"** %".19"
  %".166" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".160"
  %".167" = bitcast %"struct.LinkedNode"* %".166" to i8*
  call void @"free"(i8* %".167")
  br label %".27"
.28.if:
  %".227" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".22"
  %".228" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".227", %"struct.LinkedNode"** %".228"
  %".230" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".227", i64 0, i32 8
  %".231" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".230"
  %".232" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".228"
  %".233" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".213"
  %".234" = call %"struct.LinkedNode"* %".231"(%"struct.LinkedNode"* %".232", %"struct.LinkedNode"* %".233")
  br label %".28.endif"
.28.endif:
  %".236" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".237" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".236", i64 0, i32 3
  %".238" = load i64, i64* %".237"
  %".239" = icmp eq i64 %".238", 1
  %".240" = select  i1 %".239", i64 1, i64 0
  %".241" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".22"
  %".242" = ptrtoint %"struct.LinkedNode"* %".241" to i64
  %".243" = icmp eq i64 %".242", 0
  %".244" = select  i1 %".243", i64 1, i64 0
  %".245" = mul i64 %".240", %".244"
  %".246" = icmp eq i64 %".245", 1
  br i1 %".246", label %".28.endif.if", label %".28.endif.endif"
.28.endif.if:
  %".248" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".213"
  store %"struct.LinkedNode"* %".248", %"struct.LinkedNode"** %".22"
  br label %".28.endif.endif"
.28.endif.endif:
  %".251" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".252" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".251", i64 0, i32 3
  %".253" = load i64, i64* %".252"
  %".254" = icmp eq i64 %".253", 0
  %".255" = select  i1 %".254", i64 1, i64 0
  %".256" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".25"
  %".257" = ptrtoint %"struct.LinkedNode"* %".256" to i64
  %".258" = icmp ne i64 %".257", 0
  %".259" = select  i1 %".258", i64 1, i64 0
  %".260" = mul i64 %".255", %".259"
  %".261" = icmp eq i64 %".260", 1
  br i1 %".261", label %".28.endif.endif.if", label %".28.endif.endif.endif"
.28.endif.endif.if:
  %".263" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".25"
  %".264" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".263", %"struct.LinkedNode"** %".264"
  %".266" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".263", i64 0, i32 8
  %".267" = load %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".266"
  %".268" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".264"
  %".269" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".213"
  %".270" = call %"struct.LinkedNode"* %".267"(%"struct.LinkedNode"* %".268", %"struct.LinkedNode"* %".269")
  br label %".28.endif.endif.endif"
.28.endif.endif.endif:
  %".272" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".273" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".272", i64 0, i32 3
  %".274" = load i64, i64* %".273"
  %".275" = icmp eq i64 %".274", 0
  %".276" = select  i1 %".275", i64 1, i64 0
  %".277" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".25"
  %".278" = ptrtoint %"struct.LinkedNode"* %".277" to i64
  %".279" = icmp eq i64 %".278", 0
  %".280" = select  i1 %".279", i64 1, i64 0
  %".281" = mul i64 %".276", %".280"
  %".282" = icmp eq i64 %".281", 1
  br i1 %".282", label %".28.endif.endif.endif.if", label %".28.endif.endif.endif.endif"
.28.endif.endif.endif.if:
  %".284" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".213"
  store %"struct.LinkedNode"* %".284", %"struct.LinkedNode"** %".25"
  br label %".28.endif.endif.endif.endif"
.28.endif.endif.endif.endif:
  %".287" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".19"
  %".288" = bitcast %"struct.LinkedNode"* %".287" to i8*
  call void @"free"(i8* %".288")
  %".290" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".25"
  %".291" = ptrtoint %"struct.LinkedNode"* %".290" to i64
  %".292" = icmp ne i64 %".291", 0
  %".293" = select  i1 %".292", i64 1, i64 0
  %".294" = icmp eq i64 %".293", 1
  br i1 %".294", label %".28.endif.endif.endif.endif.if", label %".28.endif.endif.endif.endif.endif"
.28.endif.endif.endif.endif.if:
  %".296" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".25"
  %".297" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".296", %"struct.LinkedNode"** %".297"
  %".299" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".296", i64 0, i32 12
  %".300" = load void (%"struct.LinkedNode"*)*, void (%"struct.LinkedNode"*)** %".299"
  %".301" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".297"
  call void %".300"(%"struct.LinkedNode"* %".301")
  br label %".28.endif.endif.endif.endif.endif"
.28.endif.endif.endif.endif.endif:
  %".304" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".22"
  %".305" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".306" = getelementptr %"struct.GC", %"struct.GC"* %".305", i64 0, i32 0
  store %"struct.LinkedNode"* %".304", %"struct.LinkedNode"** %".306"
  %".308" = load %"struct.GC"*, %"struct.GC"** %".4"
  ret %"struct.GC"* %".308"
}

define void @"end2776533135764484139140385254920912"(%"struct.GC"* %".1")
{
.3:
  %".4" = alloca %"struct.GC"*
  store %"struct.GC"* %".1", %"struct.GC"** %".4"
  %".6" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".7" = getelementptr %"struct.GC", %"struct.GC"* %".6", i64 0, i32 0
  %".8" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".7"
  %".9" = ptrtoint %"struct.LinkedNode"* %".8" to i64
  %".10" = icmp ne i64 %".9", 0
  %".11" = select  i1 %".10", i64 1, i64 0
  %".12" = icmp eq i64 %".11", 1
  br i1 %".12", label %".3.if", label %".3.endif"
.3.if:
  %".14" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".15" = getelementptr %"struct.GC", %"struct.GC"* %".14", i64 0, i32 0
  %".16" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".15"
  %".17" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".16", %"struct.LinkedNode"** %".17"
  %".19" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".16", i64 0, i32 12
  %".20" = load void (%"struct.LinkedNode"*)*, void (%"struct.LinkedNode"*)** %".19"
  %".21" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".17"
  call void %".20"(%"struct.LinkedNode"* %".21")
  br label %".3.endif"
.3.endif:
  %".24" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".25" = getelementptr %"struct.GC", %"struct.GC"* %".24", i64 0, i32 1
  %".26" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".25"
  %".27" = ptrtoint %"struct.LinkedNode"* %".26" to i64
  %".28" = icmp ne i64 %".27", 0
  %".29" = select  i1 %".28", i64 1, i64 0
  %".30" = icmp eq i64 %".29", 1
  br i1 %".30", label %".3.endif.if", label %".3.endif.endif"
.3.endif.if:
  %".32" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".33" = getelementptr %"struct.GC", %"struct.GC"* %".32", i64 0, i32 1
  %".34" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".33"
  %".35" = alloca %"struct.LinkedNode"*
  store %"struct.LinkedNode"* %".34", %"struct.LinkedNode"** %".35"
  %".37" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".34", i64 0, i32 7
  %".38" = load i64 (%"struct.LinkedNode"*)*, i64 (%"struct.LinkedNode"*)** %".37"
  %".39" = load %"struct.LinkedNode"*, %"struct.LinkedNode"** %".35"
  %".40" = call i64 %".38"(%"struct.LinkedNode"* %".39")
  %".41" = alloca i64
  store i64 %".40", i64* %".41"
  br label %".43"
.3.endif.endif:
  %".64" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".65" = bitcast %"struct.GC"* %".64" to i8*
  call void @"free"(i8* %".65")
  ret void
.43:
  %".47" = load i64, i64* %".41"
  %".48" = icmp ne i64 %".47", 0
  %".49" = select  i1 %".48", i64 1, i64 0
  %".50" = icmp eq i64 %".49", 1
  br i1 %".50", label %".45", label %".44"
.44:
  br label %".3.endif.endif"
.45:
  %".52" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".53" = alloca %"struct.GC"*
  store %"struct.GC"* %".52", %"struct.GC"** %".53"
  %".55" = getelementptr %"struct.GC", %"struct.GC"* %".52", i64 0, i32 5
  %".56" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".55"
  %".57" = load %"struct.GC"*, %"struct.GC"** %".53"
  %".58" = call %"struct.GC"* %".56"(%"struct.GC"* %".57")
  %".59" = load i64, i64* %".41"
  %".60" = sub i64 %".59", 1
  store i64 %".60", i64* %".41"
  br label %".43"
}

@"gc140385254185936" = internal global %"struct.GC"* undef
@"__free140385244110304" = internal global void (i8*)* undef
define %"struct.Integer"* @"start531472774041103830140385250178432"(%"struct.Integer"* %".1", i64 %".2")
{
.4:
  %".5" = alloca %"struct.Integer"*
  store %"struct.Integer"* %".1", %"struct.Integer"** %".5"
  %".7" = alloca i64
  store i64 %".2", i64* %".7"
  %".9" = load i64, i64* %".7"
  %".10" = load %"struct.Integer"*, %"struct.Integer"** %".5"
  %".11" = getelementptr %"struct.Integer", %"struct.Integer"* %".10", i64 0, i32 0
  store i64 %".9", i64* %".11"
  %".13" = load %"struct.GC"*, %"struct.GC"** @"gc140385254185936"
  %".14" = alloca %"struct.GC"*
  store %"struct.GC"* %".13", %"struct.GC"** %".14"
  %".16" = getelementptr %"struct.GC", %"struct.GC"* %".13", i64 0, i32 7
  %".17" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".16"
  %".18" = load %"struct.GC"*, %"struct.GC"** %".14"
  %".19" = call %"struct.GC"* %".17"(%"struct.GC"* %".18")
  %".20" = alloca %"struct.GC"*
  store %"struct.GC"* %".19", %"struct.GC"** %".20"
  %".22" = getelementptr %"struct.GC", %"struct.GC"* %".19", i64 0, i32 9
  %".23" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".22"
  %".24" = load %"struct.GC"*, %"struct.GC"** %".20"
  %".25" = call %"struct.GC"* %".23"(%"struct.GC"* %".24")
  %".26" = load %"struct.Integer"*, %"struct.Integer"** %".5"
  ret %"struct.Integer"* %".26"
}

define void @"end2866543489059026448140385250409632"(%"struct.Integer"* %".1")
{
.3:
  %".4" = alloca %"struct.Integer"*
  store %"struct.Integer"* %".1", %"struct.Integer"** %".4"
  ret void
}

define %"struct.Integer"* @"startAllInteger140385258486800"(%"struct.Integer"* %".1", i64 %".2")
{
.4:
  %".5" = alloca %"struct.Integer"*
  store %"struct.Integer"* %".1", %"struct.Integer"** %".5"
  %".7" = alloca i64
  store i64 %".2", i64* %".7"
  br label %".9"
.9:
  %".13" = load i64, i64* %".7"
  %".14" = icmp ne i64 %".13", 0
  %".15" = select  i1 %".14", i64 1, i64 0
  %".16" = icmp eq i64 %".15", 1
  br i1 %".16", label %".11", label %".10"
.10:
  %".31" = load %"struct.Integer"*, %"struct.Integer"** %".5"
  ret %"struct.Integer"* %".31"
.11:
  %".18" = load i64, i64* %".7"
  %".19" = sub i64 %".18", 1
  store i64 %".19", i64* %".7"
  %".21" = load %"struct.Integer"*, %"struct.Integer"** %".5"
  %".22" = load i64, i64* %".7"
  %".23" = getelementptr %"struct.Integer", %"struct.Integer"* %".21", i64 %".22"
  %".24" = alloca %"struct.Integer"*
  store %"struct.Integer"* %".23", %"struct.Integer"** %".24"
  %".26" = getelementptr %"struct.Integer", %"struct.Integer"* %".23", i64 0, i32 1
  %".27" = load %"struct.Integer"* (%"struct.Integer"*, i64)*, %"struct.Integer"* (%"struct.Integer"*, i64)** %".26"
  %".28" = load %"struct.Integer"*, %"struct.Integer"** %".24"
  %".29" = call %"struct.Integer"* %".27"(%"struct.Integer"* %".28", i64 10)
  br label %".9"
}

define %"struct.IntArray"* @"start3410642138140759866140385256700992"(%"struct.IntArray"* %".1", i64 %".2")
{
.4:
  %".5" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".1", %"struct.IntArray"** %".5"
  %".7" = alloca i64
  store i64 %".2", i64* %".7"
  %".9" = load i64, i64* %".7"
  %".10" = load %"struct.IntArray"*, %"struct.IntArray"** %".5"
  %".11" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".10", i64 0, i32 1
  store i64 %".9", i64* %".11"
  %".13" = load %"struct.GC"*, %"struct.GC"** @"gc140385254185936"
  %".14" = alloca %"struct.GC"*
  store %"struct.GC"* %".13", %"struct.GC"** %".14"
  %".16" = getelementptr %"struct.GC", %"struct.GC"* %".13", i64 0, i32 3
  %".17" = load i8* (%"struct.GC"*, i8*, i64)*, i8* (%"struct.GC"*, i8*, i64)** %".16"
  %".18" = load %"struct.GC"*, %"struct.GC"** %".14"
  %".19" = load i64, i64* %".7"
  %".20" = inttoptr i64 0 to %"struct.Integer"*
  %".21" = getelementptr %"struct.Integer", %"struct.Integer"* %".20", i32 1
  %".22" = ptrtoint %"struct.Integer"* %".21" to i64
  %".23" = mul i64 %".19", %".22"
  %".24" = call i8* @"malloc"(i64 %".23")
  %".25" = alloca %"struct.Integer"
  %".26" = getelementptr %"struct.Integer", %"struct.Integer"* %".25", i64 0, i32 1
  store %"struct.Integer"* (%"struct.Integer"*, i64)* @"start531472774041103830140385250178432", %"struct.Integer"* (%"struct.Integer"*, i64)** %".26"
  %".28" = getelementptr %"struct.Integer", %"struct.Integer"* %".25", i64 0, i32 2
  store void (%"struct.Integer"*)* @"end2866543489059026448140385250409632", void (%"struct.Integer"*)** %".28"
  %".30" = bitcast %"struct.Integer"* %".25" to i8*
  %".31" = inttoptr i64 0 to %"struct.Integer"*
  %".32" = getelementptr %"struct.Integer", %"struct.Integer"* %".31", i32 1
  %".33" = ptrtoint %"struct.Integer"* %".32" to i64
  %".34" = load i64, i64* %".7"
  %".35" = call i8* @"memcpyn140385253191072"(i8* %".24", i8* %".30", i64 %".33", i64 %".34")
  %".36" = load i64, i64* %".7"
  %".37" = inttoptr i64 0 to %"struct.Integer"*
  %".38" = getelementptr %"struct.Integer", %"struct.Integer"* %".37", i32 1
  %".39" = ptrtoint %"struct.Integer"* %".38" to i64
  %".40" = mul i64 %".36", %".39"
  %".41" = call i8* %".17"(%"struct.GC"* %".18", i8* %".35", i64 %".40")
  %".42" = bitcast i8* %".41" to %"struct.Integer"*
  %".43" = load i64, i64* %".7"
  %".44" = call %"struct.Integer"* @"startAllInteger140385258486800"(%"struct.Integer"* %".42", i64 %".43")
  %".45" = load %"struct.IntArray"*, %"struct.IntArray"** %".5"
  %".46" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".45", i64 0, i32 0
  store %"struct.Integer"* %".44", %"struct.Integer"** %".46"
  %".48" = load %"struct.GC"*, %"struct.GC"** @"gc140385254185936"
  %".49" = alloca %"struct.GC"*
  store %"struct.GC"* %".48", %"struct.GC"** %".49"
  %".51" = getelementptr %"struct.GC", %"struct.GC"* %".48", i64 0, i32 5
  %".52" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".51"
  %".53" = load %"struct.GC"*, %"struct.GC"** %".49"
  %".54" = call %"struct.GC"* %".52"(%"struct.GC"* %".53")
  %".55" = load %"struct.GC"*, %"struct.GC"** @"gc140385254185936"
  %".56" = alloca %"struct.GC"*
  store %"struct.GC"* %".55", %"struct.GC"** %".56"
  %".58" = getelementptr %"struct.GC", %"struct.GC"* %".55", i64 0, i32 7
  %".59" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".58"
  %".60" = load %"struct.GC"*, %"struct.GC"** %".56"
  %".61" = call %"struct.GC"* %".59"(%"struct.GC"* %".60")
  %".62" = alloca %"struct.GC"*
  store %"struct.GC"* %".61", %"struct.GC"** %".62"
  %".64" = getelementptr %"struct.GC", %"struct.GC"* %".61", i64 0, i32 9
  %".65" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".64"
  %".66" = load %"struct.GC"*, %"struct.GC"** %".62"
  %".67" = call %"struct.GC"* %".65"(%"struct.GC"* %".66")
  %".68" = load %"struct.IntArray"*, %"struct.IntArray"** %".5"
  ret %"struct.IntArray"* %".68"
}

define void @"end3186444395447460709140385253092528"(%"struct.IntArray"* %".1")
{
.3:
  %".4" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".1", %"struct.IntArray"** %".4"
  ret void
}

define i64 @"start140385253085280"()
{
.2:
  store i8* (i8*, i8*, i64)* @"memcpy", i8* (i8*, i8*, i64)** @"__memcpy140385256897888"
  store i8* (i64)* @"malloc", i8* (i64)** @"__malloc140385251988752"
  store void (i8*)* @"free", void (i8*)** @"__free140385259166384"
  store i8* (i8*, i8*, i64)* @"memcpy", i8* (i8*, i8*, i64)** @"__memcpy140385250703392"
  store i8* (i64)* @"malloc", i8* (i64)** @"__malloc140385250699696"
  store void (i8*)* @"free", void (i8*)** @"__free140385250702192"
  store void (i8*)* @"free", void (i8*)** @"__free140385254917408"
  %".10" = inttoptr i64 0 to %"struct.GC"*
  store %"struct.GC"* %".10", %"struct.GC"** @"gc140385254185936"
  store void (i8*)* @"free", void (i8*)** @"__free140385244110304"
  br label %".13"
.13:
  %".14" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140385256897888"
  %".15" = load i8* (i64)*, i8* (i64)** @"__malloc140385251988752"
  %".16" = inttoptr i64 0 to %"struct.GC"*
  %".17" = getelementptr %"struct.GC", %"struct.GC"* %".16", i32 1
  %".18" = ptrtoint %"struct.GC"* %".17" to i64
  %".19" = call i8* %".15"(i64 %".18")
  %".20" = alloca %"struct.GC"
  %".21" = getelementptr %"struct.GC", %"struct.GC"* %".20", i64 0, i32 2
  store %"struct.GC"* (%"struct.GC"*)* @"start7835992373913572580140385256715312", %"struct.GC"* (%"struct.GC"*)** %".21"
  %".23" = getelementptr %"struct.GC", %"struct.GC"* %".20", i64 0, i32 3
  store i8* (%"struct.GC"*, i8*, i64)* @"push6196927396915817214140385256710320", i8* (%"struct.GC"*, i8*, i64)** %".23"
  %".25" = getelementptr %"struct.GC", %"struct.GC"* %".20", i64 0, i32 4
  store i8* (%"struct.GC"*, i8*, i64)* @"pushNoRoot3847600348900564826140385255537920", i8* (%"struct.GC"*, i8*, i64)** %".25"
  %".27" = getelementptr %"struct.GC", %"struct.GC"* %".20", i64 0, i32 5
  store %"struct.GC"* (%"struct.GC"*)* @"pop4268654653910679871140385252978848", %"struct.GC"* (%"struct.GC"*)** %".27"
  %".29" = getelementptr %"struct.GC", %"struct.GC"* %".20", i64 0, i32 6
  store %"struct.GC"* (%"struct.GC"*, i8*)* @"mark_root7785180052072167530140385255689808", %"struct.GC"* (%"struct.GC"*, i8*)** %".29"
  %".31" = getelementptr %"struct.GC", %"struct.GC"* %".20", i64 0, i32 7
  store %"struct.GC"* (%"struct.GC"*)* @"mark3850657141341536777140385253218128", %"struct.GC"* (%"struct.GC"*)** %".31"
  %".33" = getelementptr %"struct.GC", %"struct.GC"* %".20", i64 0, i32 8
  store %"struct.GC"* (%"struct.GC"*)* @"unmark8713185513450541210140385244202368", %"struct.GC"* (%"struct.GC"*)** %".33"
  %".35" = getelementptr %"struct.GC", %"struct.GC"* %".20", i64 0, i32 9
  store %"struct.GC"* (%"struct.GC"*)* @"sweep8665498114076620315140385244216768", %"struct.GC"* (%"struct.GC"*)** %".35"
  %".37" = getelementptr %"struct.GC", %"struct.GC"* %".20", i64 0, i32 10
  store void (%"struct.GC"*)* @"end2776533135764484139140385254920912", void (%"struct.GC"*)** %".37"
  %".39" = bitcast %"struct.GC"* %".20" to i8*
  %".40" = inttoptr i64 0 to %"struct.GC"*
  %".41" = getelementptr %"struct.GC", %"struct.GC"* %".40", i32 1
  %".42" = ptrtoint %"struct.GC"* %".41" to i64
  %".43" = call i8* %".14"(i8* %".19", i8* %".39", i64 %".42")
  %".44" = bitcast i8* %".43" to %"struct.GC"*
  %".45" = alloca %"struct.GC"*
  store %"struct.GC"* %".44", %"struct.GC"** %".45"
  %".47" = getelementptr %"struct.GC", %"struct.GC"* %".44", i64 0, i32 2
  %".48" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".47"
  %".49" = load %"struct.GC"*, %"struct.GC"** %".45"
  %".50" = call %"struct.GC"* %".48"(%"struct.GC"* %".49")
  store %"struct.GC"* %".50", %"struct.GC"** @"gc140385254185936"
  %".52" = load %"struct.GC"*, %"struct.GC"** @"gc140385254185936"
  %".53" = alloca %"struct.GC"*
  store %"struct.GC"* %".52", %"struct.GC"** %".53"
  %".55" = getelementptr %"struct.GC", %"struct.GC"* %".52", i64 0, i32 3
  %".56" = load i8* (%"struct.GC"*, i8*, i64)*, i8* (%"struct.GC"*, i8*, i64)** %".55"
  %".57" = load %"struct.GC"*, %"struct.GC"** %".53"
  %".58" = inttoptr i64 0 to %"struct.IntArray"*
  %".59" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".58", i32 1
  %".60" = ptrtoint %"struct.IntArray"* %".59" to i64
  %".61" = call i8* @"malloc"(i64 %".60")
  %".62" = alloca %"struct.IntArray"
  %".63" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".62", i64 0, i32 2
  store %"struct.IntArray"* (%"struct.IntArray"*, i64)* @"start3410642138140759866140385256700992", %"struct.IntArray"* (%"struct.IntArray"*, i64)** %".63"
  %".65" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".62", i64 0, i32 3
  store void (%"struct.IntArray"*)* @"end3186444395447460709140385253092528", void (%"struct.IntArray"*)** %".65"
  %".67" = bitcast %"struct.IntArray"* %".62" to i8*
  %".68" = inttoptr i64 0 to %"struct.IntArray"*
  %".69" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".68", i32 1
  %".70" = ptrtoint %"struct.IntArray"* %".69" to i64
  %".71" = call i8* @"memcpy"(i8* %".61", i8* %".67", i64 %".70")
  %".72" = inttoptr i64 0 to %"struct.IntArray"*
  %".73" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".72", i32 1
  %".74" = ptrtoint %"struct.IntArray"* %".73" to i64
  %".75" = call i8* %".56"(%"struct.GC"* %".57", i8* %".71", i64 %".74")
  %".76" = bitcast i8* %".75" to %"struct.IntArray"*
  %".77" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".76", %"struct.IntArray"** %".77"
  %".79" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".76", %"struct.IntArray"** %".79"
  %".81" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".76", i64 0, i32 2
  %".82" = load %"struct.IntArray"* (%"struct.IntArray"*, i64)*, %"struct.IntArray"* (%"struct.IntArray"*, i64)** %".81"
  %".83" = load %"struct.IntArray"*, %"struct.IntArray"** %".79"
  %".84" = call %"struct.IntArray"* %".82"(%"struct.IntArray"* %".83", i64 100)
  %".85" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".84", %"struct.IntArray"** %".85"
  %".87" = load %"struct.GC"*, %"struct.GC"** @"gc140385254185936"
  %".88" = alloca %"struct.GC"*
  store %"struct.GC"* %".87", %"struct.GC"** %".88"
  %".90" = getelementptr %"struct.GC", %"struct.GC"* %".87", i64 0, i32 5
  %".91" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".90"
  %".92" = load %"struct.GC"*, %"struct.GC"** %".88"
  %".93" = call %"struct.GC"* %".91"(%"struct.GC"* %".92")
  %".94" = alloca i64
  store i64 0, i64* %".94"
  %".96" = load %"struct.GC"*, %"struct.GC"** @"gc140385254185936"
  %".97" = alloca %"struct.GC"*
  store %"struct.GC"* %".96", %"struct.GC"** %".97"
  %".99" = getelementptr %"struct.GC", %"struct.GC"* %".96", i64 0, i32 10
  %".100" = load void (%"struct.GC"*)*, void (%"struct.GC"*)** %".99"
  %".101" = load %"struct.GC"*, %"struct.GC"** %".97"
  call void %".100"(%"struct.GC"* %".101")
  %".103" = load i64, i64* %".94"
  ret i64 %".103"
}

@".1" = internal unnamed_addr constant [46 x i8] c"LinkedNode(ptr:%d,elem:%d,size:%d,marked:%d)\0a\00", align 1
@".2" = internal unnamed_addr constant [37 x i8] c"MARKED ============================\0a\00", align 1