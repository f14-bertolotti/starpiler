; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

%"struct.LinkedNode" = type {%"struct.LinkedNode"*, i8*, i64, i64, %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)*, i64 (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*)*, i64 (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*)*, %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)*, void (%"struct.LinkedNode"*)*}
%"struct.GC" = type {%"struct.LinkedNode"*, %"struct.LinkedNode"*, %"struct.GC"* (%"struct.GC"*)*, i8* (%"struct.GC"*, i8*, i64)*, i8* (%"struct.GC"*, i8*, i64)*, %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*, i8*)*, %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)*, void (%"struct.GC"*)*}
%"struct.Integer" = type {i64, %"struct.Integer"* (%"struct.Integer"*, i64)*, %"struct.Integer"* (%"struct.Integer"*, i64)*, void (%"struct.Integer"*)*}
%"struct.IntArray" = type {%"struct.Integer"*, i64, %"struct.IntArray"* (%"struct.IntArray"*, i64)*, %"struct.IntArray"* (%"struct.IntArray"*, i64)*, i64 (%"struct.IntArray"*, i64)*, i64 ()*, void (%"struct.IntArray"*)*}
%"struct.IntMatrix" = type {%"struct.IntArray"*, i64, %"struct.IntMatrix"* (%"struct.IntMatrix"*, i64)*, %"struct.IntMatrix"* (%"struct.IntMatrix"*, i64)*, i64 (%"struct.IntMatrix"*, i64, i64)*, void (%"struct.IntMatrix"*)*}
declare i8* @"memcpy"(i8* %".1", i8* %".2", i64 %".3")

@"__memcpy140025685707264" = internal global i8* (i8*, i8*, i64)* undef
declare i8* @"malloc"(i64 %".1")

@"__malloc140025686035952" = internal global i8* (i64)* undef
declare void @"free"(i8* %".1")

@"__free140025682908576" = internal global void (i8*)* undef
@"__memcpy140025685802336" = internal global i8* (i8*, i8*, i64)* undef
@"__malloc140025685790096" = internal global i8* (i64)* undef
@"__free140025685794320" = internal global void (i8*)* undef
@"__free140025671281456" = internal global void (i8*)* undef
declare i64 @"printf"(i8* %".1", ...)

define %"struct.LinkedNode"* @"start8620025311489462560140025678257056"(%"struct.LinkedNode"* %".1", i8* %".2", i64 %".3")
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

define i64 @"isLast6879295095430132489140025677733968"(%"struct.LinkedNode"* %".1")
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

define %"struct.LinkedNode"* @"getLast7333906764530695109140025677735120"(%"struct.LinkedNode"* %".1")
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

define i64 @"size1002614812778670913140025677737376"(%"struct.LinkedNode"* %".1")
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

define %"struct.LinkedNode"* @"append5371002347867584402140025677553696"(%"struct.LinkedNode"* %".1", %"struct.LinkedNode"* %".2")
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

define %"struct.LinkedNode"* @"print1313748053002905345140025677550192"(%"struct.LinkedNode"* %".1")
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

define %"struct.LinkedNode"* @"printAll5158120827698798404140025677551728"(%"struct.LinkedNode"* %".1")
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

define %"struct.LinkedNode"* @"fromElementPointer4148647018684311458140025677852112"(%"struct.LinkedNode"* %".1", i8* %".2")
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

define void @"end5790104933725533744140025677854512"(%"struct.LinkedNode"* %".1")
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

define i8* @"memcpyn140025672032816"(i8* %".1", i8* %".2", i64 %".3", i64 %".4")
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

define %"struct.GC"* @"start2310914050218772307140025673054048"(%"struct.GC"* %".1")
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

define i8* @"push3986780939554197602140025673040128"(%"struct.GC"* %".1", i8* %".2", i64 %".3")
{
.5:
  %".6" = alloca %"struct.GC"*
  store %"struct.GC"* %".1", %"struct.GC"** %".6"
  %".8" = alloca i8*
  store i8* %".2", i8** %".8"
  %".10" = alloca i64
  store i64 %".3", i64* %".10"
  %".12" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140025685802336"
  %".13" = load i8* (i64)*, i8* (i64)** @"__malloc140025685790096"
  %".14" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".15" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".14", i32 1
  %".16" = ptrtoint %"struct.LinkedNode"* %".15" to i64
  %".17" = call i8* %".13"(i64 %".16")
  %".18" = alloca %"struct.LinkedNode"
  %".19" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 4
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)* @"start8620025311489462560140025678257056", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".19"
  %".21" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 5
  store i64 (%"struct.LinkedNode"*)* @"isLast6879295095430132489140025677733968", i64 (%"struct.LinkedNode"*)** %".21"
  %".23" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 6
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"getLast7333906764530695109140025677735120", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".23"
  %".25" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 7
  store i64 (%"struct.LinkedNode"*)* @"size1002614812778670913140025677737376", i64 (%"struct.LinkedNode"*)** %".25"
  %".27" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 8
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)* @"append5371002347867584402140025677553696", %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".27"
  %".29" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 9
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"print1313748053002905345140025677550192", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".29"
  %".31" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 10
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"printAll5158120827698798404140025677551728", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".31"
  %".33" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 11
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)* @"fromElementPointer4148647018684311458140025677852112", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".33"
  %".35" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 12
  store void (%"struct.LinkedNode"*)* @"end5790104933725533744140025677854512", void (%"struct.LinkedNode"*)** %".35"
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
  %".53" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140025685802336"
  %".54" = load i8* (i64)*, i8* (i64)** @"__malloc140025685790096"
  %".55" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".56" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".55", i32 1
  %".57" = ptrtoint %"struct.LinkedNode"* %".56" to i64
  %".58" = call i8* %".54"(i64 %".57")
  %".59" = alloca %"struct.LinkedNode"
  %".60" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 4
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)* @"start8620025311489462560140025678257056", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".60"
  %".62" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 5
  store i64 (%"struct.LinkedNode"*)* @"isLast6879295095430132489140025677733968", i64 (%"struct.LinkedNode"*)** %".62"
  %".64" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 6
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"getLast7333906764530695109140025677735120", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".64"
  %".66" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 7
  store i64 (%"struct.LinkedNode"*)* @"size1002614812778670913140025677737376", i64 (%"struct.LinkedNode"*)** %".66"
  %".68" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 8
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)* @"append5371002347867584402140025677553696", %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".68"
  %".70" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 9
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"print1313748053002905345140025677550192", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".70"
  %".72" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 10
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"printAll5158120827698798404140025677551728", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".72"
  %".74" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 11
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)* @"fromElementPointer4148647018684311458140025677852112", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".74"
  %".76" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".59", i64 0, i32 12
  store void (%"struct.LinkedNode"*)* @"end5790104933725533744140025677854512", void (%"struct.LinkedNode"*)** %".76"
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

define i8* @"pushNoRoot865399480220097422140025672583344"(%"struct.GC"* %".1", i8* %".2", i64 %".3")
{
.5:
  %".6" = alloca %"struct.GC"*
  store %"struct.GC"* %".1", %"struct.GC"** %".6"
  %".8" = alloca i8*
  store i8* %".2", i8** %".8"
  %".10" = alloca i64
  store i64 %".3", i64* %".10"
  %".12" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140025685802336"
  %".13" = load i8* (i64)*, i8* (i64)** @"__malloc140025685790096"
  %".14" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".15" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".14", i32 1
  %".16" = ptrtoint %"struct.LinkedNode"* %".15" to i64
  %".17" = call i8* %".13"(i64 %".16")
  %".18" = alloca %"struct.LinkedNode"
  %".19" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 4
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)* @"start8620025311489462560140025678257056", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".19"
  %".21" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 5
  store i64 (%"struct.LinkedNode"*)* @"isLast6879295095430132489140025677733968", i64 (%"struct.LinkedNode"*)** %".21"
  %".23" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 6
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"getLast7333906764530695109140025677735120", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".23"
  %".25" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 7
  store i64 (%"struct.LinkedNode"*)* @"size1002614812778670913140025677737376", i64 (%"struct.LinkedNode"*)** %".25"
  %".27" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 8
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)* @"append5371002347867584402140025677553696", %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".27"
  %".29" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 9
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"print1313748053002905345140025677550192", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".29"
  %".31" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 10
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"printAll5158120827698798404140025677551728", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".31"
  %".33" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 11
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)* @"fromElementPointer4148647018684311458140025677852112", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".33"
  %".35" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".18", i64 0, i32 12
  store void (%"struct.LinkedNode"*)* @"end5790104933725533744140025677854512", void (%"struct.LinkedNode"*)** %".35"
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

define %"struct.GC"* @"pop5799783159106790810140025672488880"(%"struct.GC"* %".1")
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

define %"struct.GC"* @"mark_root3312316270777276926140025671512656"(%"struct.GC"* %".1", i8* %".2")
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

define %"struct.GC"* @"mark3147247675627971187140025672046128"(%"struct.GC"* %".1")
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

define %"struct.GC"* @"unmark1701363724752337086140025672049200"(%"struct.GC"* %".1")
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

define %"struct.GC"* @"sweep7064879577693495656140025674786048"(%"struct.GC"* %".1")
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
  %".170" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140025685802336"
  %".171" = load i8* (i64)*, i8* (i64)** @"__malloc140025685790096"
  %".172" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".173" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".172", i32 1
  %".174" = ptrtoint %"struct.LinkedNode"* %".173" to i64
  %".175" = call i8* %".171"(i64 %".174")
  %".176" = alloca %"struct.LinkedNode"
  %".177" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 4
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)* @"start8620025311489462560140025678257056", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".177"
  %".179" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 5
  store i64 (%"struct.LinkedNode"*)* @"isLast6879295095430132489140025677733968", i64 (%"struct.LinkedNode"*)** %".179"
  %".181" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 6
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"getLast7333906764530695109140025677735120", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".181"
  %".183" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 7
  store i64 (%"struct.LinkedNode"*)* @"size1002614812778670913140025677737376", i64 (%"struct.LinkedNode"*)** %".183"
  %".185" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 8
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)* @"append5371002347867584402140025677553696", %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".185"
  %".187" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 9
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"print1313748053002905345140025677550192", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".187"
  %".189" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 10
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"printAll5158120827698798404140025677551728", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".189"
  %".191" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 11
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)* @"fromElementPointer4148647018684311458140025677852112", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".191"
  %".193" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".176", i64 0, i32 12
  store void (%"struct.LinkedNode"*)* @"end5790104933725533744140025677854512", void (%"struct.LinkedNode"*)** %".193"
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
  %".42" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140025685802336"
  %".43" = load i8* (i64)*, i8* (i64)** @"__malloc140025685790096"
  %".44" = inttoptr i64 0 to %"struct.LinkedNode"*
  %".45" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".44", i32 1
  %".46" = ptrtoint %"struct.LinkedNode"* %".45" to i64
  %".47" = call i8* %".43"(i64 %".46")
  %".48" = alloca %"struct.LinkedNode"
  %".49" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 4
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)* @"start8620025311489462560140025678257056", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*, i64)** %".49"
  %".51" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 5
  store i64 (%"struct.LinkedNode"*)* @"isLast6879295095430132489140025677733968", i64 (%"struct.LinkedNode"*)** %".51"
  %".53" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 6
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"getLast7333906764530695109140025677735120", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".53"
  %".55" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 7
  store i64 (%"struct.LinkedNode"*)* @"size1002614812778670913140025677737376", i64 (%"struct.LinkedNode"*)** %".55"
  %".57" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 8
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)* @"append5371002347867584402140025677553696", %"struct.LinkedNode"* (%"struct.LinkedNode"*, %"struct.LinkedNode"*)** %".57"
  %".59" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 9
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"print1313748053002905345140025677550192", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".59"
  %".61" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 10
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*)* @"printAll5158120827698798404140025677551728", %"struct.LinkedNode"* (%"struct.LinkedNode"*)** %".61"
  %".63" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 11
  store %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)* @"fromElementPointer4148647018684311458140025677852112", %"struct.LinkedNode"* (%"struct.LinkedNode"*, i8*)** %".63"
  %".65" = getelementptr %"struct.LinkedNode", %"struct.LinkedNode"* %".48", i64 0, i32 12
  store void (%"struct.LinkedNode"*)* @"end5790104933725533744140025677854512", void (%"struct.LinkedNode"*)** %".65"
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

define void @"end4599559715011540059140025671412336"(%"struct.GC"* %".1")
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

@"gc140025672395664" = internal global %"struct.GC"* undef
@"__free140025680366560" = internal global void (i8*)* undef
define %"struct.Integer"* @"start5036314534789325321140025672715904"(%"struct.Integer"* %".1", i64 %".2")
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
  %".13" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
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

define %"struct.Integer"* @"set3986402647827263801140025681276656"(%"struct.Integer"* %".1", i64 %".2")
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
  %".13" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
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

define void @"end8520518278740942162140025681277328"(%"struct.Integer"* %".1")
{
.3:
  %".4" = alloca %"struct.Integer"*
  store %"struct.Integer"* %".1", %"struct.Integer"** %".4"
  ret void
}

@"__free140025672037472" = internal global void (i8*)* undef
define %"struct.Integer"* @"startAllInteger140025686495568"(%"struct.Integer"* %".1", i64 %".2")
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
  %".29" = call %"struct.Integer"* %".27"(%"struct.Integer"* %".28", i64 0)
  br label %".9"
}

define %"struct.IntArray"* @"start66419056223115765140025672388128"(%"struct.IntArray"* %".1", i64 %".2")
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
  %".13" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
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
  store %"struct.Integer"* (%"struct.Integer"*, i64)* @"start5036314534789325321140025672715904", %"struct.Integer"* (%"struct.Integer"*, i64)** %".26"
  %".28" = getelementptr %"struct.Integer", %"struct.Integer"* %".25", i64 0, i32 2
  store %"struct.Integer"* (%"struct.Integer"*, i64)* @"set3986402647827263801140025681276656", %"struct.Integer"* (%"struct.Integer"*, i64)** %".28"
  %".30" = getelementptr %"struct.Integer", %"struct.Integer"* %".25", i64 0, i32 3
  store void (%"struct.Integer"*)* @"end8520518278740942162140025681277328", void (%"struct.Integer"*)** %".30"
  %".32" = bitcast %"struct.Integer"* %".25" to i8*
  %".33" = inttoptr i64 0 to %"struct.Integer"*
  %".34" = getelementptr %"struct.Integer", %"struct.Integer"* %".33", i32 1
  %".35" = ptrtoint %"struct.Integer"* %".34" to i64
  %".36" = load i64, i64* %".7"
  %".37" = call i8* @"memcpyn140025672032816"(i8* %".24", i8* %".32", i64 %".35", i64 %".36")
  %".38" = load i64, i64* %".7"
  %".39" = inttoptr i64 0 to %"struct.Integer"*
  %".40" = getelementptr %"struct.Integer", %"struct.Integer"* %".39", i32 1
  %".41" = ptrtoint %"struct.Integer"* %".40" to i64
  %".42" = mul i64 %".38", %".41"
  %".43" = call i8* %".17"(%"struct.GC"* %".18", i8* %".37", i64 %".42")
  %".44" = bitcast i8* %".43" to %"struct.Integer"*
  %".45" = load i64, i64* %".7"
  %".46" = call %"struct.Integer"* @"startAllInteger140025686495568"(%"struct.Integer"* %".44", i64 %".45")
  %".47" = load %"struct.IntArray"*, %"struct.IntArray"** %".5"
  %".48" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".47", i64 0, i32 0
  store %"struct.Integer"* %".46", %"struct.Integer"** %".48"
  %".50" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".51" = alloca %"struct.GC"*
  store %"struct.GC"* %".50", %"struct.GC"** %".51"
  %".53" = getelementptr %"struct.GC", %"struct.GC"* %".50", i64 0, i32 7
  %".54" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".53"
  %".55" = load %"struct.GC"*, %"struct.GC"** %".51"
  %".56" = call %"struct.GC"* %".54"(%"struct.GC"* %".55")
  %".57" = alloca %"struct.GC"*
  store %"struct.GC"* %".56", %"struct.GC"** %".57"
  %".59" = getelementptr %"struct.GC", %"struct.GC"* %".56", i64 0, i32 9
  %".60" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".59"
  %".61" = load %"struct.GC"*, %"struct.GC"** %".57"
  %".62" = call %"struct.GC"* %".60"(%"struct.GC"* %".61")
  %".63" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".64" = alloca %"struct.GC"*
  store %"struct.GC"* %".63", %"struct.GC"** %".64"
  %".66" = getelementptr %"struct.GC", %"struct.GC"* %".63", i64 0, i32 5
  %".67" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".66"
  %".68" = load %"struct.GC"*, %"struct.GC"** %".64"
  %".69" = call %"struct.GC"* %".67"(%"struct.GC"* %".68")
  %".70" = load %"struct.IntArray"*, %"struct.IntArray"** %".5"
  ret %"struct.IntArray"* %".70"
}

define %"struct.IntArray"* @"fill7421250275187907067140025675087104"(%"struct.IntArray"* %".1", i64 %".2")
{
.4:
  %".5" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".1", %"struct.IntArray"** %".5"
  %".7" = alloca i64
  store i64 %".2", i64* %".7"
  %".9" = alloca i64
  store i64 0, i64* %".9"
  br label %".11"
.11:
  %".15" = load i64, i64* %".9"
  %".16" = load %"struct.IntArray"*, %"struct.IntArray"** %".5"
  %".17" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".16", i64 0, i32 1
  %".18" = load i64, i64* %".17"
  %".19" = icmp slt i64 %".15", %".18"
  %".20" = select  i1 %".19", i64 1, i64 0
  %".21" = icmp eq i64 %".20", 1
  br i1 %".21", label %".13", label %".12"
.12:
  %".35" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".36" = alloca %"struct.GC"*
  store %"struct.GC"* %".35", %"struct.GC"** %".36"
  %".38" = getelementptr %"struct.GC", %"struct.GC"* %".35", i64 0, i32 7
  %".39" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".38"
  %".40" = load %"struct.GC"*, %"struct.GC"** %".36"
  %".41" = call %"struct.GC"* %".39"(%"struct.GC"* %".40")
  %".42" = alloca %"struct.GC"*
  store %"struct.GC"* %".41", %"struct.GC"** %".42"
  %".44" = getelementptr %"struct.GC", %"struct.GC"* %".41", i64 0, i32 9
  %".45" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".44"
  %".46" = load %"struct.GC"*, %"struct.GC"** %".42"
  %".47" = call %"struct.GC"* %".45"(%"struct.GC"* %".46")
  %".48" = load %"struct.IntArray"*, %"struct.IntArray"** %".5"
  ret %"struct.IntArray"* %".48"
.13:
  %".23" = load i64, i64* %".7"
  %".24" = load %"struct.IntArray"*, %"struct.IntArray"** %".5"
  %".25" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".24", i64 0, i32 0
  %".26" = load %"struct.Integer"*, %"struct.Integer"** %".25"
  %".27" = load i64, i64* %".9"
  %".28" = getelementptr %"struct.Integer", %"struct.Integer"* %".26", i64 %".27"
  %".29" = getelementptr %"struct.Integer", %"struct.Integer"* %".28", i64 0, i32 0
  store i64 %".23", i64* %".29"
  %".31" = load i64, i64* %".9"
  %".32" = add i64 %".31", 1
  store i64 %".32", i64* %".9"
  br label %".11"
}

define i64 @"get8170834176515953252140025675076976"(%"struct.IntArray"* %".1", i64 %".2")
{
.4:
  %".5" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".1", %"struct.IntArray"** %".5"
  %".7" = alloca i64
  store i64 %".2", i64* %".7"
  %".9" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".10" = alloca %"struct.GC"*
  store %"struct.GC"* %".9", %"struct.GC"** %".10"
  %".12" = getelementptr %"struct.GC", %"struct.GC"* %".9", i64 0, i32 7
  %".13" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".12"
  %".14" = load %"struct.GC"*, %"struct.GC"** %".10"
  %".15" = call %"struct.GC"* %".13"(%"struct.GC"* %".14")
  %".16" = alloca %"struct.GC"*
  store %"struct.GC"* %".15", %"struct.GC"** %".16"
  %".18" = getelementptr %"struct.GC", %"struct.GC"* %".15", i64 0, i32 9
  %".19" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".18"
  %".20" = load %"struct.GC"*, %"struct.GC"** %".16"
  %".21" = call %"struct.GC"* %".19"(%"struct.GC"* %".20")
  %".22" = load %"struct.IntArray"*, %"struct.IntArray"** %".5"
  %".23" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".22", i64 0, i32 0
  %".24" = load %"struct.Integer"*, %"struct.Integer"** %".23"
  %".25" = load i64, i64* %".7"
  %".26" = getelementptr %"struct.Integer", %"struct.Integer"* %".24", i64 %".25"
  %".27" = getelementptr %"struct.Integer", %"struct.Integer"* %".26", i64 0, i32 0
  %".28" = load i64, i64* %".27"
  ret i64 %".28"
}

define i64 @"__main__5036869651598450773140025675086672"()
{
.2:
  %".3" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".4" = alloca %"struct.GC"*
  store %"struct.GC"* %".3", %"struct.GC"** %".4"
  %".6" = getelementptr %"struct.GC", %"struct.GC"* %".3", i64 0, i32 3
  %".7" = load i8* (%"struct.GC"*, i8*, i64)*, i8* (%"struct.GC"*, i8*, i64)** %".6"
  %".8" = load %"struct.GC"*, %"struct.GC"** %".4"
  %".9" = inttoptr i64 0 to %"struct.IntArray"*
  %".10" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".9", i32 1
  %".11" = ptrtoint %"struct.IntArray"* %".10" to i64
  %".12" = call i8* @"malloc"(i64 %".11")
  %".13" = alloca %"struct.IntArray"
  %".14" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".13", i64 0, i32 2
  store %"struct.IntArray"* (%"struct.IntArray"*, i64)* @"start66419056223115765140025672388128", %"struct.IntArray"* (%"struct.IntArray"*, i64)** %".14"
  %".16" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".13", i64 0, i32 3
  store %"struct.IntArray"* (%"struct.IntArray"*, i64)* @"fill7421250275187907067140025675087104", %"struct.IntArray"* (%"struct.IntArray"*, i64)** %".16"
  %".18" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".13", i64 0, i32 4
  store i64 (%"struct.IntArray"*, i64)* @"get8170834176515953252140025675076976", i64 (%"struct.IntArray"*, i64)** %".18"
  %".20" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".13", i64 0, i32 5
  store i64 ()* @"__main__5036869651598450773140025675086672", i64 ()** %".20"
  %".22" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".13", i64 0, i32 6
  store void (%"struct.IntArray"*)* @"end5444752471678964963140025675081488", void (%"struct.IntArray"*)** %".22"
  %".24" = bitcast %"struct.IntArray"* %".13" to i8*
  %".25" = inttoptr i64 0 to %"struct.IntArray"*
  %".26" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".25", i32 1
  %".27" = ptrtoint %"struct.IntArray"* %".26" to i64
  %".28" = call i8* @"memcpy"(i8* %".12", i8* %".24", i64 %".27")
  %".29" = inttoptr i64 0 to %"struct.IntArray"*
  %".30" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".29", i32 1
  %".31" = ptrtoint %"struct.IntArray"* %".30" to i64
  %".32" = call i8* %".7"(%"struct.GC"* %".8", i8* %".28", i64 %".31")
  %".33" = bitcast i8* %".32" to %"struct.IntArray"*
  %".34" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".33", %"struct.IntArray"** %".34"
  %".36" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".33", %"struct.IntArray"** %".36"
  %".38" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".33", i64 0, i32 2
  %".39" = load %"struct.IntArray"* (%"struct.IntArray"*, i64)*, %"struct.IntArray"* (%"struct.IntArray"*, i64)** %".38"
  %".40" = load %"struct.IntArray"*, %"struct.IntArray"** %".36"
  %".41" = call %"struct.IntArray"* %".39"(%"struct.IntArray"* %".40", i64 100)
  %".42" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".41", %"struct.IntArray"** %".42"
  %".44" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".41", i64 0, i32 3
  %".45" = load %"struct.IntArray"* (%"struct.IntArray"*, i64)*, %"struct.IntArray"* (%"struct.IntArray"*, i64)** %".44"
  %".46" = load %"struct.IntArray"*, %"struct.IntArray"** %".42"
  %".47" = call %"struct.IntArray"* %".45"(%"struct.IntArray"* %".46", i64 10)
  %".48" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".47", %"struct.IntArray"** %".48"
  %".50" = alloca i64
  store i64 0, i64* %".50"
  %".52" = alloca i64
  store i64 1, i64* %".52"
  br label %".54"
.54:
  %".58" = load i64, i64* %".50"
  %".59" = load %"struct.IntArray"*, %"struct.IntArray"** %".48"
  %".60" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".59", i64 0, i32 1
  %".61" = load i64, i64* %".60"
  %".62" = icmp slt i64 %".58", %".61"
  %".63" = select  i1 %".62", i64 1, i64 0
  %".64" = icmp eq i64 %".63", 1
  br i1 %".64", label %".56", label %".55"
.55:
  %".83" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".84" = alloca %"struct.GC"*
  store %"struct.GC"* %".83", %"struct.GC"** %".84"
  %".86" = getelementptr %"struct.GC", %"struct.GC"* %".83", i64 0, i32 7
  %".87" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".86"
  %".88" = load %"struct.GC"*, %"struct.GC"** %".84"
  %".89" = call %"struct.GC"* %".87"(%"struct.GC"* %".88")
  %".90" = alloca %"struct.GC"*
  store %"struct.GC"* %".89", %"struct.GC"** %".90"
  %".92" = getelementptr %"struct.GC", %"struct.GC"* %".89", i64 0, i32 9
  %".93" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".92"
  %".94" = load %"struct.GC"*, %"struct.GC"** %".90"
  %".95" = call %"struct.GC"* %".93"(%"struct.GC"* %".94")
  %".96" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".97" = alloca %"struct.GC"*
  store %"struct.GC"* %".96", %"struct.GC"** %".97"
  %".99" = getelementptr %"struct.GC", %"struct.GC"* %".96", i64 0, i32 5
  %".100" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".99"
  %".101" = load %"struct.GC"*, %"struct.GC"** %".97"
  %".102" = call %"struct.GC"* %".100"(%"struct.GC"* %".101")
  %".103" = load i64, i64* %".52"
  ret i64 %".103"
.56:
  %".66" = load i64, i64* %".52"
  %".67" = load %"struct.IntArray"*, %"struct.IntArray"** %".48"
  %".68" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".67", %"struct.IntArray"** %".68"
  %".70" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".67", i64 0, i32 4
  %".71" = load i64 (%"struct.IntArray"*, i64)*, i64 (%"struct.IntArray"*, i64)** %".70"
  %".72" = load %"struct.IntArray"*, %"struct.IntArray"** %".68"
  %".73" = load i64, i64* %".50"
  %".74" = call i64 %".71"(%"struct.IntArray"* %".72", i64 %".73")
  %".75" = icmp eq i64 %".74", 10
  %".76" = select  i1 %".75", i64 1, i64 0
  %".77" = mul i64 %".66", %".76"
  store i64 %".77", i64* %".52"
  %".79" = load i64, i64* %".50"
  %".80" = add i64 %".79", 1
  store i64 %".80", i64* %".50"
  br label %".54"
}

define void @"end5444752471678964963140025675081488"(%"struct.IntArray"* %".1")
{
.3:
  %".4" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".1", %"struct.IntArray"** %".4"
  ret void
}

define %"struct.IntArray"* @"startAllIntArray140025687147856"(%"struct.IntArray"* %".1", i64 %".2")
{
.4:
  %".5" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".1", %"struct.IntArray"** %".5"
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
  %".32" = load %"struct.IntArray"*, %"struct.IntArray"** %".5"
  ret %"struct.IntArray"* %".32"
.11:
  %".18" = load i64, i64* %".7"
  %".19" = sub i64 %".18", 1
  store i64 %".19", i64* %".7"
  %".21" = load %"struct.IntArray"*, %"struct.IntArray"** %".5"
  %".22" = load i64, i64* %".7"
  %".23" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".21", i64 %".22"
  %".24" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".23", %"struct.IntArray"** %".24"
  %".26" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".23", i64 0, i32 2
  %".27" = load %"struct.IntArray"* (%"struct.IntArray"*, i64)*, %"struct.IntArray"* (%"struct.IntArray"*, i64)** %".26"
  %".28" = load %"struct.IntArray"*, %"struct.IntArray"** %".24"
  %".29" = load i64, i64* %".7"
  %".30" = call %"struct.IntArray"* %".27"(%"struct.IntArray"* %".28", i64 %".29")
  br label %".9"
}

define %"struct.IntMatrix"* @"start5525493451056975730140025687158080"(%"struct.IntMatrix"* %".1", i64 %".2")
{
.4:
  %".5" = alloca %"struct.IntMatrix"*
  store %"struct.IntMatrix"* %".1", %"struct.IntMatrix"** %".5"
  %".7" = alloca i64
  store i64 %".2", i64* %".7"
  %".9" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".10" = alloca %"struct.GC"*
  store %"struct.GC"* %".9", %"struct.GC"** %".10"
  %".12" = getelementptr %"struct.GC", %"struct.GC"* %".9", i64 0, i32 3
  %".13" = load i8* (%"struct.GC"*, i8*, i64)*, i8* (%"struct.GC"*, i8*, i64)** %".12"
  %".14" = load %"struct.GC"*, %"struct.GC"** %".10"
  %".15" = load i64, i64* %".7"
  %".16" = inttoptr i64 0 to %"struct.IntArray"*
  %".17" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".16", i32 1
  %".18" = ptrtoint %"struct.IntArray"* %".17" to i64
  %".19" = mul i64 %".15", %".18"
  %".20" = call i8* @"malloc"(i64 %".19")
  %".21" = alloca %"struct.IntArray"
  %".22" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".21", i64 0, i32 2
  store %"struct.IntArray"* (%"struct.IntArray"*, i64)* @"start66419056223115765140025672388128", %"struct.IntArray"* (%"struct.IntArray"*, i64)** %".22"
  %".24" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".21", i64 0, i32 3
  store %"struct.IntArray"* (%"struct.IntArray"*, i64)* @"fill7421250275187907067140025675087104", %"struct.IntArray"* (%"struct.IntArray"*, i64)** %".24"
  %".26" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".21", i64 0, i32 4
  store i64 (%"struct.IntArray"*, i64)* @"get8170834176515953252140025675076976", i64 (%"struct.IntArray"*, i64)** %".26"
  %".28" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".21", i64 0, i32 5
  store i64 ()* @"__main__5036869651598450773140025675086672", i64 ()** %".28"
  %".30" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".21", i64 0, i32 6
  store void (%"struct.IntArray"*)* @"end5444752471678964963140025675081488", void (%"struct.IntArray"*)** %".30"
  %".32" = bitcast %"struct.IntArray"* %".21" to i8*
  %".33" = inttoptr i64 0 to %"struct.IntArray"*
  %".34" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".33", i32 1
  %".35" = ptrtoint %"struct.IntArray"* %".34" to i64
  %".36" = load i64, i64* %".7"
  %".37" = call i8* @"memcpyn140025672032816"(i8* %".20", i8* %".32", i64 %".35", i64 %".36")
  %".38" = load i64, i64* %".7"
  %".39" = inttoptr i64 0 to %"struct.IntArray"*
  %".40" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".39", i32 1
  %".41" = ptrtoint %"struct.IntArray"* %".40" to i64
  %".42" = mul i64 %".38", %".41"
  %".43" = call i8* %".13"(%"struct.GC"* %".14", i8* %".37", i64 %".42")
  %".44" = bitcast i8* %".43" to %"struct.IntArray"*
  %".45" = load i64, i64* %".7"
  %".46" = call %"struct.IntArray"* @"startAllIntArray140025687147856"(%"struct.IntArray"* %".44", i64 %".45")
  %".47" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".5"
  %".48" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".47", i64 0, i32 0
  store %"struct.IntArray"* %".46", %"struct.IntArray"** %".48"
  %".50" = load i64, i64* %".7"
  %".51" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".5"
  %".52" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".51", i64 0, i32 1
  store i64 %".50", i64* %".52"
  %".54" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".55" = alloca %"struct.GC"*
  store %"struct.GC"* %".54", %"struct.GC"** %".55"
  %".57" = getelementptr %"struct.GC", %"struct.GC"* %".54", i64 0, i32 5
  %".58" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".57"
  %".59" = load %"struct.GC"*, %"struct.GC"** %".55"
  %".60" = call %"struct.GC"* %".58"(%"struct.GC"* %".59")
  %".61" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".62" = alloca %"struct.GC"*
  store %"struct.GC"* %".61", %"struct.GC"** %".62"
  %".64" = getelementptr %"struct.GC", %"struct.GC"* %".61", i64 0, i32 7
  %".65" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".64"
  %".66" = load %"struct.GC"*, %"struct.GC"** %".62"
  %".67" = call %"struct.GC"* %".65"(%"struct.GC"* %".66")
  %".68" = alloca %"struct.GC"*
  store %"struct.GC"* %".67", %"struct.GC"** %".68"
  %".70" = getelementptr %"struct.GC", %"struct.GC"* %".67", i64 0, i32 9
  %".71" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".70"
  %".72" = load %"struct.GC"*, %"struct.GC"** %".68"
  %".73" = call %"struct.GC"* %".71"(%"struct.GC"* %".72")
  %".74" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".5"
  ret %"struct.IntMatrix"* %".74"
}

define %"struct.IntMatrix"* @"fill8161044153312145258140025685309040"(%"struct.IntMatrix"* %".1", i64 %".2")
{
.4:
  %".5" = alloca %"struct.IntMatrix"*
  store %"struct.IntMatrix"* %".1", %"struct.IntMatrix"** %".5"
  %".7" = alloca i64
  store i64 %".2", i64* %".7"
  %".9" = alloca i64
  store i64 0, i64* %".9"
  br label %".11"
.11:
  %".15" = load i64, i64* %".9"
  %".16" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".5"
  %".17" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".16", i64 0, i32 1
  %".18" = load i64, i64* %".17"
  %".19" = icmp slt i64 %".15", %".18"
  %".20" = select  i1 %".19", i64 1, i64 0
  %".21" = icmp eq i64 %".20", 1
  br i1 %".21", label %".13", label %".12"
.12:
  %".39" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".40" = alloca %"struct.GC"*
  store %"struct.GC"* %".39", %"struct.GC"** %".40"
  %".42" = getelementptr %"struct.GC", %"struct.GC"* %".39", i64 0, i32 7
  %".43" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".42"
  %".44" = load %"struct.GC"*, %"struct.GC"** %".40"
  %".45" = call %"struct.GC"* %".43"(%"struct.GC"* %".44")
  %".46" = alloca %"struct.GC"*
  store %"struct.GC"* %".45", %"struct.GC"** %".46"
  %".48" = getelementptr %"struct.GC", %"struct.GC"* %".45", i64 0, i32 9
  %".49" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".48"
  %".50" = load %"struct.GC"*, %"struct.GC"** %".46"
  %".51" = call %"struct.GC"* %".49"(%"struct.GC"* %".50")
  %".52" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".5"
  ret %"struct.IntMatrix"* %".52"
.13:
  %".23" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".5"
  %".24" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".23", i64 0, i32 0
  %".25" = load %"struct.IntArray"*, %"struct.IntArray"** %".24"
  %".26" = load i64, i64* %".9"
  %".27" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".25", i64 %".26"
  %".28" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".27", %"struct.IntArray"** %".28"
  %".30" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".27", i64 0, i32 3
  %".31" = load %"struct.IntArray"* (%"struct.IntArray"*, i64)*, %"struct.IntArray"* (%"struct.IntArray"*, i64)** %".30"
  %".32" = load %"struct.IntArray"*, %"struct.IntArray"** %".28"
  %".33" = load i64, i64* %".7"
  %".34" = call %"struct.IntArray"* %".31"(%"struct.IntArray"* %".32", i64 %".33")
  %".35" = load i64, i64* %".9"
  %".36" = add i64 %".35", 1
  store i64 %".36", i64* %".9"
  br label %".11"
}

define i64 @"get3085805827505500439140025685799408"(%"struct.IntMatrix"* %".1", i64 %".2", i64 %".3")
{
.5:
  %".6" = alloca %"struct.IntMatrix"*
  store %"struct.IntMatrix"* %".1", %"struct.IntMatrix"** %".6"
  %".8" = alloca i64
  store i64 %".2", i64* %".8"
  %".10" = alloca i64
  store i64 %".3", i64* %".10"
  %".12" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".13" = alloca %"struct.GC"*
  store %"struct.GC"* %".12", %"struct.GC"** %".13"
  %".15" = getelementptr %"struct.GC", %"struct.GC"* %".12", i64 0, i32 7
  %".16" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".15"
  %".17" = load %"struct.GC"*, %"struct.GC"** %".13"
  %".18" = call %"struct.GC"* %".16"(%"struct.GC"* %".17")
  %".19" = alloca %"struct.GC"*
  store %"struct.GC"* %".18", %"struct.GC"** %".19"
  %".21" = getelementptr %"struct.GC", %"struct.GC"* %".18", i64 0, i32 9
  %".22" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".21"
  %".23" = load %"struct.GC"*, %"struct.GC"** %".19"
  %".24" = call %"struct.GC"* %".22"(%"struct.GC"* %".23")
  %".25" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".6"
  %".26" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".25", i64 0, i32 0
  %".27" = load %"struct.IntArray"*, %"struct.IntArray"** %".26"
  %".28" = load i64, i64* %".8"
  %".29" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".27", i64 %".28"
  %".30" = alloca %"struct.IntArray"*
  store %"struct.IntArray"* %".29", %"struct.IntArray"** %".30"
  %".32" = getelementptr %"struct.IntArray", %"struct.IntArray"* %".29", i64 0, i32 4
  %".33" = load i64 (%"struct.IntArray"*, i64)*, i64 (%"struct.IntArray"*, i64)** %".32"
  %".34" = load %"struct.IntArray"*, %"struct.IntArray"** %".30"
  %".35" = load i64, i64* %".10"
  %".36" = call i64 %".33"(%"struct.IntArray"* %".34", i64 %".35")
  ret i64 %".36"
}

define void @"end4570020498782467464140025691315920"(%"struct.IntMatrix"* %".1")
{
.3:
  %".4" = alloca %"struct.IntMatrix"*
  store %"struct.IntMatrix"* %".1", %"struct.IntMatrix"** %".4"
  ret void
}

define i64 @"start140025691316400"()
{
.2:
  store i8* (i8*, i8*, i64)* @"memcpy", i8* (i8*, i8*, i64)** @"__memcpy140025685707264"
  store i8* (i64)* @"malloc", i8* (i64)** @"__malloc140025686035952"
  store void (i8*)* @"free", void (i8*)** @"__free140025682908576"
  store i8* (i8*, i8*, i64)* @"memcpy", i8* (i8*, i8*, i64)** @"__memcpy140025685802336"
  store i8* (i64)* @"malloc", i8* (i64)** @"__malloc140025685790096"
  store void (i8*)* @"free", void (i8*)** @"__free140025685794320"
  store void (i8*)* @"free", void (i8*)** @"__free140025671281456"
  %".10" = inttoptr i64 0 to %"struct.GC"*
  store %"struct.GC"* %".10", %"struct.GC"** @"gc140025672395664"
  store void (i8*)* @"free", void (i8*)** @"__free140025680366560"
  store void (i8*)* @"free", void (i8*)** @"__free140025672037472"
  br label %".14"
.14:
  %".15" = load i8* (i8*, i8*, i64)*, i8* (i8*, i8*, i64)** @"__memcpy140025685707264"
  %".16" = load i8* (i64)*, i8* (i64)** @"__malloc140025686035952"
  %".17" = inttoptr i64 0 to %"struct.GC"*
  %".18" = getelementptr %"struct.GC", %"struct.GC"* %".17", i32 1
  %".19" = ptrtoint %"struct.GC"* %".18" to i64
  %".20" = call i8* %".16"(i64 %".19")
  %".21" = alloca %"struct.GC"
  %".22" = getelementptr %"struct.GC", %"struct.GC"* %".21", i64 0, i32 2
  store %"struct.GC"* (%"struct.GC"*)* @"start2310914050218772307140025673054048", %"struct.GC"* (%"struct.GC"*)** %".22"
  %".24" = getelementptr %"struct.GC", %"struct.GC"* %".21", i64 0, i32 3
  store i8* (%"struct.GC"*, i8*, i64)* @"push3986780939554197602140025673040128", i8* (%"struct.GC"*, i8*, i64)** %".24"
  %".26" = getelementptr %"struct.GC", %"struct.GC"* %".21", i64 0, i32 4
  store i8* (%"struct.GC"*, i8*, i64)* @"pushNoRoot865399480220097422140025672583344", i8* (%"struct.GC"*, i8*, i64)** %".26"
  %".28" = getelementptr %"struct.GC", %"struct.GC"* %".21", i64 0, i32 5
  store %"struct.GC"* (%"struct.GC"*)* @"pop5799783159106790810140025672488880", %"struct.GC"* (%"struct.GC"*)** %".28"
  %".30" = getelementptr %"struct.GC", %"struct.GC"* %".21", i64 0, i32 6
  store %"struct.GC"* (%"struct.GC"*, i8*)* @"mark_root3312316270777276926140025671512656", %"struct.GC"* (%"struct.GC"*, i8*)** %".30"
  %".32" = getelementptr %"struct.GC", %"struct.GC"* %".21", i64 0, i32 7
  store %"struct.GC"* (%"struct.GC"*)* @"mark3147247675627971187140025672046128", %"struct.GC"* (%"struct.GC"*)** %".32"
  %".34" = getelementptr %"struct.GC", %"struct.GC"* %".21", i64 0, i32 8
  store %"struct.GC"* (%"struct.GC"*)* @"unmark1701363724752337086140025672049200", %"struct.GC"* (%"struct.GC"*)** %".34"
  %".36" = getelementptr %"struct.GC", %"struct.GC"* %".21", i64 0, i32 9
  store %"struct.GC"* (%"struct.GC"*)* @"sweep7064879577693495656140025674786048", %"struct.GC"* (%"struct.GC"*)** %".36"
  %".38" = getelementptr %"struct.GC", %"struct.GC"* %".21", i64 0, i32 10
  store void (%"struct.GC"*)* @"end4599559715011540059140025671412336", void (%"struct.GC"*)** %".38"
  %".40" = bitcast %"struct.GC"* %".21" to i8*
  %".41" = inttoptr i64 0 to %"struct.GC"*
  %".42" = getelementptr %"struct.GC", %"struct.GC"* %".41", i32 1
  %".43" = ptrtoint %"struct.GC"* %".42" to i64
  %".44" = call i8* %".15"(i8* %".20", i8* %".40", i64 %".43")
  %".45" = bitcast i8* %".44" to %"struct.GC"*
  %".46" = alloca %"struct.GC"*
  store %"struct.GC"* %".45", %"struct.GC"** %".46"
  %".48" = getelementptr %"struct.GC", %"struct.GC"* %".45", i64 0, i32 2
  %".49" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".48"
  %".50" = load %"struct.GC"*, %"struct.GC"** %".46"
  %".51" = call %"struct.GC"* %".49"(%"struct.GC"* %".50")
  store %"struct.GC"* %".51", %"struct.GC"** @"gc140025672395664"
  %".53" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".54" = alloca %"struct.GC"*
  store %"struct.GC"* %".53", %"struct.GC"** %".54"
  %".56" = getelementptr %"struct.GC", %"struct.GC"* %".53", i64 0, i32 3
  %".57" = load i8* (%"struct.GC"*, i8*, i64)*, i8* (%"struct.GC"*, i8*, i64)** %".56"
  %".58" = load %"struct.GC"*, %"struct.GC"** %".54"
  %".59" = inttoptr i64 0 to %"struct.IntMatrix"*
  %".60" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".59", i32 1
  %".61" = ptrtoint %"struct.IntMatrix"* %".60" to i64
  %".62" = call i8* @"malloc"(i64 %".61")
  %".63" = alloca %"struct.IntMatrix"
  %".64" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".63", i64 0, i32 2
  store %"struct.IntMatrix"* (%"struct.IntMatrix"*, i64)* @"start5525493451056975730140025687158080", %"struct.IntMatrix"* (%"struct.IntMatrix"*, i64)** %".64"
  %".66" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".63", i64 0, i32 3
  store %"struct.IntMatrix"* (%"struct.IntMatrix"*, i64)* @"fill8161044153312145258140025685309040", %"struct.IntMatrix"* (%"struct.IntMatrix"*, i64)** %".66"
  %".68" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".63", i64 0, i32 4
  store i64 (%"struct.IntMatrix"*, i64, i64)* @"get3085805827505500439140025685799408", i64 (%"struct.IntMatrix"*, i64, i64)** %".68"
  %".70" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".63", i64 0, i32 5
  store void (%"struct.IntMatrix"*)* @"end4570020498782467464140025691315920", void (%"struct.IntMatrix"*)** %".70"
  %".72" = bitcast %"struct.IntMatrix"* %".63" to i8*
  %".73" = inttoptr i64 0 to %"struct.IntMatrix"*
  %".74" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".73", i32 1
  %".75" = ptrtoint %"struct.IntMatrix"* %".74" to i64
  %".76" = call i8* @"memcpy"(i8* %".62", i8* %".72", i64 %".75")
  %".77" = inttoptr i64 0 to %"struct.IntMatrix"*
  %".78" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".77", i32 1
  %".79" = ptrtoint %"struct.IntMatrix"* %".78" to i64
  %".80" = call i8* %".57"(%"struct.GC"* %".58", i8* %".76", i64 %".79")
  %".81" = bitcast i8* %".80" to %"struct.IntMatrix"*
  %".82" = alloca %"struct.IntMatrix"*
  store %"struct.IntMatrix"* %".81", %"struct.IntMatrix"** %".82"
  %".84" = alloca %"struct.IntMatrix"*
  store %"struct.IntMatrix"* %".81", %"struct.IntMatrix"** %".84"
  %".86" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".81", i64 0, i32 2
  %".87" = load %"struct.IntMatrix"* (%"struct.IntMatrix"*, i64)*, %"struct.IntMatrix"* (%"struct.IntMatrix"*, i64)** %".86"
  %".88" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".84"
  %".89" = call %"struct.IntMatrix"* %".87"(%"struct.IntMatrix"* %".88", i64 10)
  %".90" = alloca %"struct.IntMatrix"*
  store %"struct.IntMatrix"* %".89", %"struct.IntMatrix"** %".90"
  %".92" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".89", i64 0, i32 3
  %".93" = load %"struct.IntMatrix"* (%"struct.IntMatrix"*, i64)*, %"struct.IntMatrix"* (%"struct.IntMatrix"*, i64)** %".92"
  %".94" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".90"
  %".95" = call %"struct.IntMatrix"* %".93"(%"struct.IntMatrix"* %".94", i64 1)
  %".96" = alloca %"struct.IntMatrix"*
  store %"struct.IntMatrix"* %".95", %"struct.IntMatrix"** %".96"
  %".98" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".99" = alloca %"struct.GC"*
  store %"struct.GC"* %".98", %"struct.GC"** %".99"
  %".101" = getelementptr %"struct.GC", %"struct.GC"* %".98", i64 0, i32 5
  %".102" = load %"struct.GC"* (%"struct.GC"*)*, %"struct.GC"* (%"struct.GC"*)** %".101"
  %".103" = load %"struct.GC"*, %"struct.GC"** %".99"
  %".104" = call %"struct.GC"* %".102"(%"struct.GC"* %".103")
  %".105" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".96"
  %".106" = alloca %"struct.IntMatrix"*
  store %"struct.IntMatrix"* %".105", %"struct.IntMatrix"** %".106"
  %".108" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".105", i64 0, i32 4
  %".109" = load i64 (%"struct.IntMatrix"*, i64, i64)*, i64 (%"struct.IntMatrix"*, i64, i64)** %".108"
  %".110" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".106"
  %".111" = call i64 %".109"(%"struct.IntMatrix"* %".110", i64 0, i64 0)
  %".112" = icmp eq i64 %".111", 1
  %".113" = select  i1 %".112", i64 1, i64 0
  %".114" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".96"
  %".115" = alloca %"struct.IntMatrix"*
  store %"struct.IntMatrix"* %".114", %"struct.IntMatrix"** %".115"
  %".117" = getelementptr %"struct.IntMatrix", %"struct.IntMatrix"* %".114", i64 0, i32 4
  %".118" = load i64 (%"struct.IntMatrix"*, i64, i64)*, i64 (%"struct.IntMatrix"*, i64, i64)** %".117"
  %".119" = load %"struct.IntMatrix"*, %"struct.IntMatrix"** %".115"
  %".120" = call i64 %".118"(%"struct.IntMatrix"* %".119", i64 9, i64 9)
  %".121" = icmp eq i64 %".120", 1
  %".122" = select  i1 %".121", i64 1, i64 0
  %".123" = mul i64 %".113", %".122"
  %".124" = alloca i64
  store i64 %".123", i64* %".124"
  %".126" = load %"struct.GC"*, %"struct.GC"** @"gc140025672395664"
  %".127" = alloca %"struct.GC"*
  store %"struct.GC"* %".126", %"struct.GC"** %".127"
  %".129" = getelementptr %"struct.GC", %"struct.GC"* %".126", i64 0, i32 10
  %".130" = load void (%"struct.GC"*)*, void (%"struct.GC"*)** %".129"
  %".131" = load %"struct.GC"*, %"struct.GC"** %".127"
  call void %".130"(%"struct.GC"* %".131")
  %".133" = load i64, i64* %".124"
  ret i64 %".133"
}

@".1" = internal unnamed_addr constant [46 x i8] c"LinkedNode(ptr:%d,elem:%d,size:%d,marked:%d)\0a\00", align 1
@".2" = internal unnamed_addr constant [37 x i8] c"MARKED ============================\0a\00", align 1