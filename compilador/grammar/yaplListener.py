# Generated from yapl.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .yaplParser import yaplParser
else:
    from yaplParser import yaplParser

# This class defines a complete listener for a parse tree produced by yaplParser.
class yaplListener(ParseTreeListener):

    # Enter a parse tree produced by yaplParser#program.
    def enterProgram(self, ctx:yaplParser.ProgramContext):
        pass

    # Exit a parse tree produced by yaplParser#program.
    def exitProgram(self, ctx:yaplParser.ProgramContext):
        pass


    # Enter a parse tree produced by yaplParser#classDeclaration.
    def enterClassDeclaration(self, ctx:yaplParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by yaplParser#classDeclaration.
    def exitClassDeclaration(self, ctx:yaplParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by yaplParser#classBody.
    def enterClassBody(self, ctx:yaplParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by yaplParser#classBody.
    def exitClassBody(self, ctx:yaplParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by yaplParser#attributeDeclaration.
    def enterAttributeDeclaration(self, ctx:yaplParser.AttributeDeclarationContext):
        pass

    # Exit a parse tree produced by yaplParser#attributeDeclaration.
    def exitAttributeDeclaration(self, ctx:yaplParser.AttributeDeclarationContext):
        pass


    # Enter a parse tree produced by yaplParser#assignmentDeclaration.
    def enterAssignmentDeclaration(self, ctx:yaplParser.AssignmentDeclarationContext):
        pass

    # Exit a parse tree produced by yaplParser#assignmentDeclaration.
    def exitAssignmentDeclaration(self, ctx:yaplParser.AssignmentDeclarationContext):
        pass


    # Enter a parse tree produced by yaplParser#type.
    def enterType(self, ctx:yaplParser.TypeContext):
        pass

    # Exit a parse tree produced by yaplParser#type.
    def exitType(self, ctx:yaplParser.TypeContext):
        pass


    # Enter a parse tree produced by yaplParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:yaplParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by yaplParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:yaplParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by yaplParser#parameterList.
    def enterParameterList(self, ctx:yaplParser.ParameterListContext):
        pass

    # Exit a parse tree produced by yaplParser#parameterList.
    def exitParameterList(self, ctx:yaplParser.ParameterListContext):
        pass


    # Enter a parse tree produced by yaplParser#parameter.
    def enterParameter(self, ctx:yaplParser.ParameterContext):
        pass

    # Exit a parse tree produced by yaplParser#parameter.
    def exitParameter(self, ctx:yaplParser.ParameterContext):
        pass


    # Enter a parse tree produced by yaplParser#statement.
    def enterStatement(self, ctx:yaplParser.StatementContext):
        pass

    # Exit a parse tree produced by yaplParser#statement.
    def exitStatement(self, ctx:yaplParser.StatementContext):
        pass


    # Enter a parse tree produced by yaplParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:yaplParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by yaplParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:yaplParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by yaplParser#letDeclaration.
    def enterLetDeclaration(self, ctx:yaplParser.LetDeclarationContext):
        pass

    # Exit a parse tree produced by yaplParser#letDeclaration.
    def exitLetDeclaration(self, ctx:yaplParser.LetDeclarationContext):
        pass


    # Enter a parse tree produced by yaplParser#ifStatement.
    def enterIfStatement(self, ctx:yaplParser.IfStatementContext):
        pass

    # Exit a parse tree produced by yaplParser#ifStatement.
    def exitIfStatement(self, ctx:yaplParser.IfStatementContext):
        pass


    # Enter a parse tree produced by yaplParser#whileStatement.
    def enterWhileStatement(self, ctx:yaplParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by yaplParser#whileStatement.
    def exitWhileStatement(self, ctx:yaplParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by yaplParser#methodCallStatement.
    def enterMethodCallStatement(self, ctx:yaplParser.MethodCallStatementContext):
        pass

    # Exit a parse tree produced by yaplParser#methodCallStatement.
    def exitMethodCallStatement(self, ctx:yaplParser.MethodCallStatementContext):
        pass


    # Enter a parse tree produced by yaplParser#expressionStatement.
    def enterExpressionStatement(self, ctx:yaplParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by yaplParser#expressionStatement.
    def exitExpressionStatement(self, ctx:yaplParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by yaplParser#returnStatement.
    def enterReturnStatement(self, ctx:yaplParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by yaplParser#returnStatement.
    def exitReturnStatement(self, ctx:yaplParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by yaplParser#expressionList.
    def enterExpressionList(self, ctx:yaplParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by yaplParser#expressionList.
    def exitExpressionList(self, ctx:yaplParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by yaplParser#block.
    def enterBlock(self, ctx:yaplParser.BlockContext):
        pass

    # Exit a parse tree produced by yaplParser#block.
    def exitBlock(self, ctx:yaplParser.BlockContext):
        pass


    # Enter a parse tree produced by yaplParser#classMethodCallExpression.
    def enterClassMethodCallExpression(self, ctx:yaplParser.ClassMethodCallExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#classMethodCallExpression.
    def exitClassMethodCallExpression(self, ctx:yaplParser.ClassMethodCallExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#additionExpression.
    def enterAdditionExpression(self, ctx:yaplParser.AdditionExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#additionExpression.
    def exitAdditionExpression(self, ctx:yaplParser.AdditionExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#lessThanOrEqualExpression.
    def enterLessThanOrEqualExpression(self, ctx:yaplParser.LessThanOrEqualExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#lessThanOrEqualExpression.
    def exitLessThanOrEqualExpression(self, ctx:yaplParser.LessThanOrEqualExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#newExpression.
    def enterNewExpression(self, ctx:yaplParser.NewExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#newExpression.
    def exitNewExpression(self, ctx:yaplParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:yaplParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:yaplParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:yaplParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:yaplParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#notExpression.
    def enterNotExpression(self, ctx:yaplParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#notExpression.
    def exitNotExpression(self, ctx:yaplParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#selfLiteralExpression.
    def enterSelfLiteralExpression(self, ctx:yaplParser.SelfLiteralExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#selfLiteralExpression.
    def exitSelfLiteralExpression(self, ctx:yaplParser.SelfLiteralExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#multiplicationExpression.
    def enterMultiplicationExpression(self, ctx:yaplParser.MultiplicationExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#multiplicationExpression.
    def exitMultiplicationExpression(self, ctx:yaplParser.MultiplicationExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#notEqualExpression.
    def enterNotEqualExpression(self, ctx:yaplParser.NotEqualExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#notEqualExpression.
    def exitNotEqualExpression(self, ctx:yaplParser.NotEqualExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#greaterThanExpression.
    def enterGreaterThanExpression(self, ctx:yaplParser.GreaterThanExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#greaterThanExpression.
    def exitGreaterThanExpression(self, ctx:yaplParser.GreaterThanExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#greaterThanOrEqualExpression.
    def enterGreaterThanOrEqualExpression(self, ctx:yaplParser.GreaterThanOrEqualExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#greaterThanOrEqualExpression.
    def exitGreaterThanOrEqualExpression(self, ctx:yaplParser.GreaterThanOrEqualExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#stringLiteralExpression.
    def enterStringLiteralExpression(self, ctx:yaplParser.StringLiteralExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#stringLiteralExpression.
    def exitStringLiteralExpression(self, ctx:yaplParser.StringLiteralExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#orExpression.
    def enterOrExpression(self, ctx:yaplParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#orExpression.
    def exitOrExpression(self, ctx:yaplParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#unaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx:yaplParser.UnaryMinusExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#unaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx:yaplParser.UnaryMinusExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#andExpression.
    def enterAndExpression(self, ctx:yaplParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#andExpression.
    def exitAndExpression(self, ctx:yaplParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#trueLiteralExpression.
    def enterTrueLiteralExpression(self, ctx:yaplParser.TrueLiteralExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#trueLiteralExpression.
    def exitTrueLiteralExpression(self, ctx:yaplParser.TrueLiteralExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#subtractionExpression.
    def enterSubtractionExpression(self, ctx:yaplParser.SubtractionExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#subtractionExpression.
    def exitSubtractionExpression(self, ctx:yaplParser.SubtractionExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#integerLiteralExpression.
    def enterIntegerLiteralExpression(self, ctx:yaplParser.IntegerLiteralExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#integerLiteralExpression.
    def exitIntegerLiteralExpression(self, ctx:yaplParser.IntegerLiteralExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#voidLiteralExpression.
    def enterVoidLiteralExpression(self, ctx:yaplParser.VoidLiteralExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#voidLiteralExpression.
    def exitVoidLiteralExpression(self, ctx:yaplParser.VoidLiteralExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#equalityExpression.
    def enterEqualityExpression(self, ctx:yaplParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#equalityExpression.
    def exitEqualityExpression(self, ctx:yaplParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#lessThanExpression.
    def enterLessThanExpression(self, ctx:yaplParser.LessThanExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#lessThanExpression.
    def exitLessThanExpression(self, ctx:yaplParser.LessThanExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#divisionExpression.
    def enterDivisionExpression(self, ctx:yaplParser.DivisionExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#divisionExpression.
    def exitDivisionExpression(self, ctx:yaplParser.DivisionExpressionContext):
        pass


    # Enter a parse tree produced by yaplParser#falseLiteralExpression.
    def enterFalseLiteralExpression(self, ctx:yaplParser.FalseLiteralExpressionContext):
        pass

    # Exit a parse tree produced by yaplParser#falseLiteralExpression.
    def exitFalseLiteralExpression(self, ctx:yaplParser.FalseLiteralExpressionContext):
        pass



del yaplParser